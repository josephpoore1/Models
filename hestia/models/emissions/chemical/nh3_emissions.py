from hestia.models.farmed_crop import FarmedCrop
from hestia.models.coefficients.conversions import Conversions
from hestia.models.references.repository import ReferencesRepository
import numpy as np


class NH3Emission:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references = references_repository

    def calculate_for(self, crop: FarmedCrop):
        instance = NH3Emission(self._references)

        self.calculate_synthetic(crop)

    def calculate_synthetic(self, crop: FarmedCrop):
        fertilizer_use = self._references.get_synth_fert_use()
        fertilizer = crop.activities.fertilizing.synthetic
        nh3_for_soil = self._references.get_nh3_for_acidic_soil() if crop.field.land.soil.phH20 <= 7 else self._references.get_nh3_for_alkaline_soil()
        temperature_index = crop.field.land.weather.get_average_temp_index()

        return crop.activities.fertilizing.synthetic.n \
               * np.dot(fertilizer_use['global'] if fertilizer.composition.sum() < 0.99 else fertilizer.composition.series(),
                        nh3_for_soil.loc[temperature_index])

    def calculate_organic(self, crop: FarmedCrop):
        nh3_tan = self._references.get_nh3_tan_from_fert()
        self.organic = crop.activities.fertilizing.organic.tan\
                       * np.dot(crop.activities.fertilizing.organic.tan_composition.to_series(), nh3_tan['organic'])

    def calculate_excreta(self, crop: FarmedCrop):
        nh3_tan = self._references.get_nh3_tan_from_fert()
        self.excreta = crop.activities.fertilizing.excreta.tan * nh3_tan['excreta'].loc[crop.activities.fertilizing.excreta.animal]

    def calculate_residue(self, crop: FarmedCrop):
        residue_shares = self._references.get_residue_est_from_dm_yield()
        atomic_weight_conversions = self._references.get_atomic_weight_conversions()

        return np.amax(
            0.38 * residue_shares.loc['n_content_ag'] * 1000 -5.44, 0
        ) / 100 * residue_shares.loc['n_content_ag'] * crop.activities.residue_management.crop_residue.above_ground_remaining \
               * atomic_weight_conversions['nh3n_nh3']


    def calculate_residue_burn(self, crop: FarmedCrop):
        res_burn = self._references.get_res_burn_emissions()
        self.residue_burn = crop.activities.residue_management.crop_residue.burnt_kg * res_burn['hn3']

