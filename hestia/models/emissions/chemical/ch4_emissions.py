from hestia.models.activities.residue_management import CropResidue
from hestia.models.farmed_crop import FarmedCrop


class CH4Emission:
    residue_burn: float

    def __init__(self):
        pass

    def create_for(self, crop: FarmedCrop):
        emission_factor = self._data['EF_Burn_DM_CH4']

        instance = CH4Emission()
        instance.residue_burn = self._get_residue_burn(crop.activities.residue_management.crop_residue, emission_factor)
        return instance

    def _get_residue_burn(self, residue: CropResidue, emission_factor):
        return residue.BurntDM * emission_factor
