from hestia.models.farmed_crop import FarmedCrop
from hestia.models.geospatial.soil import Soil
from hestia.models.activities.fertilizers.fertilizers import Fertilizers

import numpy as np
import pandas as pd

class N2OEmissions:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float
    total: float

    def __init__(self, references):
        self._references = references

    def calculate_synthetic(self, synthetic_n_amount, fertilizing_n_total):
        self.synthetic = self.total * synthetic_n_amount / fertilizing_n_total

    def calculate_organic(self, organic_n_amount, fertilizing_n_total):
        self.organic = self.total * organic_n_amount / fertilizing_n_total

    def calculate_excreta(self, excreta_n_amount, fertilizing_n_total):
        self.excreta = self.total * excreta_n_amount / fertilizing_n_total

    def calculate_residue(self, residue_amount):
        self.residue = residue_amount * self._conversions.residue.emissions.n2o

    def calculate_residue_burn(self, residue_burnt_amount):
        self.residue_burn = residue_burnt_amount * self._conversions.residue_burn.emissions.n2o

    def calculate_total(self, fertilizers: Fertilizers, soil: Soil):


        crop_n2o_n = self._references['List_IPCC_Crops_N2ON']
        self.total = np.amin(
                            0.072 * fertilizers.total_n(),
                            np.exp(
                                0.475 +
                                0.038 * fertilizers.total_n() +
                                (0 if soil.org_carbon < 0.01 else 0.526 if soil.org_carbon <= 0.03 else 0.6334) +
                                (0 if soil.phH20 < 5.5 else -0.4836 if soil.phH20 > 7.3 else -0.0693) +
                                (0 if soil.sand > 0.65 and soil.clay < 0.18 else -0.1528 if soil.sand < 0.65 and soil.clay < 0.35 else 0.4312 ) +
                                climate_n2o_n +
                                crop_n2o_n) -
                            np.exp(
                                0.475 +
                                (0 if soil.org_carbon < 0.01 else 0.526 if soil.org_carbon <= 0.03 else 0.6334) +
                                (0 if soil.phH20 < 5.5 else -0.4836 if soil.phH20 > 7.3 else -0.0693) +
                                (0 if soil.sand > 0.65 and soil.clay < 0.18 else -0.1528 if soil.sand < 0.65 and soil.clay < 0.35 else 0.4312) +
                                self._conversions.climate.c_n2o_N +
                                self._conversions.crop.emissions.c_n2o_N)) * self._conversions.atomic_weights.n2on_n2o


