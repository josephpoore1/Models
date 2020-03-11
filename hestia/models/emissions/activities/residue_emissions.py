from hestia.models.farmed_crop import FarmedCrop
from hestia.models.references.repository import ReferencesRepository
from hestia.models.emissions.chemical.chemical_emissions import ChemicalEmissions


class ResidueBurnEmissions:
    direct: float
    indirect: float
    total: float

    def __init__(self, chemical_emissions: ChemicalEmissions, references_repository: ReferencesRepository):
        self._references = references_repository
        self._chemical_emissions = chemical_emissions

    def _calculate_for(self,crop: FarmedCrop):
        self._calculate_direct(crop)
        self._calculate_indirect(crop)
        self._calculate_total(crop)

    def _calculate_direct(self, crop: FarmedCrop):
        pass

    def _calculate_indirect(self, crop: FarmedCrop):
        pass

    def _calculate_total(self, crop: FarmedCrop):
        pass