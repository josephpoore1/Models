from hestia.models.farmed_crop import FarmedCrop
from hestia.models.references.repository import ReferencesRepository
from hestia.models.emissions.chemical.chemical_emissions import ChemicalEmissions


class OrganicFertilizerEmissions:
    ch4: float

    def __init__(self, chemical_emissions: ChemicalEmissions, references_repository: ReferencesRepository):
        self._references = references_repository

    def _calculate_for(self,crop: FarmedCrop):
        self._calculate_ch4(crop)

    def _calculate_ch4(self, crop: FarmedCrop):
        pass