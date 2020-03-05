from hestia.models.farmed_crop import FarmedCrop
from hestia.models.geospatial.weather import Weather
from hestia.models.crops.crop import Crop
from hestia.models.geospatial.soil import Soil
from hestia.models.activities.fertilizers.fertilizers import Fertilizers
from hestia.models.references.repository import ReferencesRepository

import numpy as np


class N2OEmissions:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float
    total: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references = references_repository

    def calculate_for(self, farmed_crop: FarmedCrop):
        # total must be calculated first
        self.calculate_total(fertilizers= farmed_crop.activities.fertilizing,
                             soil= farmed_crop.field.land.soil,
                             weather= farmed_crop.field.land.weather)

        self.calculate_synthetic(farmed_crop.activities.fertilizing, self.total)
        self.calculate_organic(farmed_crop.activities.fertilizing, self.total)
        self.calculate_excreta(farmed_crop.activities.fertilizing, self.total)

        self.calculate_residue(farmed_crop.activities.residue_management.crop_residue.total)
        self.calculate_residue_burn(farmed_crop.activities.residue_management.crop_residue.burnt_kg)

    def calculate_synthetic(self, fertilizers: Fertilizers, n2o_total):
        self.synthetic = n2o_total * fertilizers.synthetic.n / sum(fertilizers.synthetic.n, fertilizers.organic.n, fertilizers.excreta.n)

    def calculate_organic(self, fertilizers: Fertilizers, n2o_total):
        self.organic = n2o_total * fertilizers.organic.n / sum(fertilizers.synthetic.n, fertilizers.organic.n, fertilizers.excreta.n)

    def calculate_excreta(self, fertilizers: Fertilizers, n2o_total):
        self.excreta = n2o_total * fertilizers.excreta.n / sum(fertilizers.synthetic.n, fertilizers.organic.n, fertilizers.excreta.n)

    def calculate_residue(self, residue_amount):
        residue_emissions = self._references.get_n2o_from_residue()
        self.residue = residue_amount * residue_emissions

    def calculate_residue_burn(self, residue_burnt_amount):
        residue_burn_emissions = self._references.get_res_burn_emissions()
        self.residue_burn = residue_burnt_amount * residue_burn_emissions['n2o']

    def calculate_total(self, fertilizers: Fertilizers, soil: Soil, crop: Crop, weather: Weather):
        climate_emissions = self._references.get_climate_zone_emissions()
        crop_n2o_n = self._references.get_ipcc_crop_n2o_n()
        n2on_n2o = self._references.get_default_n2o_emission_factors()

        self.total = np.amin(
                            0.072 * fertilizers.total_n(),
                            np.exp(
                                0.475 +
                                0.038 * fertilizers.total_n() +
                                (0 if soil.org_carbon < 0.01 else 0.526 if soil.org_carbon <= 0.03 else 0.6334) +
                                (0 if soil.phH20 < 5.5 else -0.4836 if soil.phH20 > 7.3 else -0.0693) +
                                (0 if soil.sand > 0.65 and soil.clay < 0.18 else -0.1528 if soil.sand < 0.65 and soil.clay < 0.35 else 0.4312 ) +
                                climate_emissions.loc[weather.eco_clim_zone.value, 'n2o_n'] + crop_n2o_n[crop.characteristics.crop_name]) -
                            np.exp(
                                0.475 +
                                (0 if soil.org_carbon < 0.01 else 0.526 if soil.org_carbon <= 0.03 else 0.6334) +
                                (0 if soil.phH20 < 5.5 else -0.4836 if soil.phH20 > 7.3 else -0.0693) +
                                (0 if soil.sand > 0.65 and soil.clay < 0.18 else -0.1528 if soil.sand < 0.65 and soil.clay < 0.35 else 0.4312) +
                                climate_emissions[weather.eco_clim_zone.value, 'n2o_n'] + crop_n2o_n[crop.characteristics.crop_name])) \
                     * n2on_n2o
