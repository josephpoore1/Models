from hestia.models.farmed_crop import FarmedCrop
from hestia.models.coefficients.conversions import Conversions
import numpy as np


class NH3Emission:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float

    def __init__(self, conversions: Conversions):
        self._conversions = conversions

    def calculate_synthetic(self, synthetic_n_amount, synthetic_n_composition, nh3_from_synt_fert):
        self.synthetic = synthetic_n_amount * np.dot(
            self._conversions.fertilizer.comp_global if np.sum(synthetic_n_composition) < 0.99 else synthetic_n_composition,
            nh3_from_synt_fert)

    def calculate_organic(self, organic_tan, organic_tan_composition):
        self.organic = organic_tan * np.dot(organic_tan_composition, self._conversions.fertilizer.organic.nh3_tan)

    def calculate_excreta(self, excreta_tan):
        try:
            self.excreta = excreta_tan * self._conversions.fertilizer.excreta.nh3_tan
        finally:
            pass

    def calculate_residue(self, crop: FarmedCrop){
        try:
            residue_n_ag = 

            np.amax(0.38 * )
        finally:
            # ToDo: log warning that we failed to calculate actual
            pass
    }

    def calculate_residue(self, residue_ag):
        self.residue = 0
        try:
            self.residue = np.amax((0.38 * self._conversions.residue.n_content_ag * 1000 -5.44, 0))\
                               / 100 *(residue_ag * self._conversions.residue.n_content_ag * self._conversions.atomic_weights.nh3n_nh3)
        finally:
            # ToDo: log warning that we failed to calculate actual
            pass

    def calculate_residue_burn(self, residue_burnt_amount):
        self.residue_burn = residue_burnt_amount * self._conversions.residue_burn.emissions.nh3

