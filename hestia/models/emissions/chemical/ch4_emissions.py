from hestia.models.references.repository import ReferencesRepository
from hestia.models.activities.residue_management import CropResidue
from hestia.models.farmed_crop import FarmedCrop


class CH4Emissions:
    residue_burn: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references = references_repository

    def calculate_for(self, crop: FarmedCrop):
        instance = CH4Emissions()
        instance.residue_burn = self._get_residue_burn(crop.activities.residue_management.crop_residue)
        return instance

    def _get_residue_burn(self, residue: CropResidue):
        emission_factors = self._references.get_res_burn_emissions()
        return residue.burnt_kg * emission_factors['ch4']
