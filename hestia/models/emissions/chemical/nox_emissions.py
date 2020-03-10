from hestia.models.farmed_crop import FarmedCrop
from hestia.models.references.repository import ReferencesRepository
import numpy as np


class NOxEmissions:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float
    total: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references = references_repository

    def calculate_for(self, crop: FarmedCrop):
        self.calculate_total(crop)

        self.calculate_organic(crop, self.total)
        self.calculate_synthetic(crop, self.total)
        self.calculate_excreta(crop, self.total)
        self.calculate_residue(crop, self.total)
        self.calculate_residue_burn(crop)

    def calculate_total(self, crop: FarmedCrop):
        default_regional_nox = self._references.get_regional_nox_emissions()
        climate_emissions = self._references.get_climate_zone_emissions()
        atomic_conversions = self._references.get_atomic_weight_conversions()

        n_total = self._get_total_n(crop)

        if crop.field.land.sp == 'A' or np.isnan(crop.field.land.sp):
            self.total = default_regional_nox.loc[crop.field.land.country] * n_total
        else:
            self.total = min(
                0.25 * n_total,
                np.exp(
                    -0.451 + 0.0061 * n_total +
                    (0 if crop.field.land.soil.nitrogen / 1000 < 0.005 else
                    -1.0211 if crop.field.land.soil.nitrogen <= 0.02 else 0.7892) +
                    climate_emissions[crop.field.land.weather.eco_clim_zone, 'nox_n']
                ) - np.exp(
                    -0.451 +
                    (0 if crop.field.land.soil.nitrogen / 1000 < 0.005 else
                     -1.0211 if crop.field.land.soil.nitrogen <= 0.02 else 0.7892) +
                    climate_emissions[crop.field.land.weather.eco_clim_zone, 'nox_n']
                )
            ) * atomic_conversions['non_no']

    def _get_total_n(self, crop):
        return sum((crop.activities.residue_management.crop_residue.total,
                   crop.activities.fertilizing.synthetic.n,
                   crop.activities.fertilizing.organic.n,
                   crop.activities.fertilizing.excreta.n))

    def calculate_synthetic(self, crop: FarmedCrop, nox_total):
        self.synthetic = nox_total * crop.activities.fertilizing.synthetic.n / self._get_total_n(crop)

    def calculate_organic(self, crop: FarmedCrop, nox_total):
        self.organic = nox_total * crop.activities.fertilizing.organic.n / self._get_total_n(crop)

    def calculate_excreta(self, crop: FarmedCrop, nox_total):
        self.excreta = nox_total * crop.activities.fertilizing.excreta.n / self._get_total_n(crop)

    def calculate_residue(self, crop: FarmedCrop, nox_total):
        self.residue = nox_total * crop.activities.residue_management.crop_residue.total / self._get_total_n(crop)

    def calculate_residue_burn(self, crop: FarmedCrop):
        residue_burn_emissions = self._references.get_res_burn_emissions()
        self.residue_burn = crop.activities.residue_management.crop_residue.burnt_kg * residue_burn_emissions['nox']


