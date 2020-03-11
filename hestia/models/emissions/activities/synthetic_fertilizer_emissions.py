from hestia.models.farmed_crop import FarmedCrop
from hestia.models.emissions.chemical.chemical_emissions import ChemicalEmissions
from hestia.models.references.repository import ReferencesRepository


class SyntheticFertilizerEmissions:
    direct: float
    indirect: float

    def __init__(self, chemical_emissions: ChemicalEmissions, references_repository: ReferencesRepository):
        self._references = references_repository
        self._emissions = chemical_emissions

    def _calculate_for(self,crop: FarmedCrop):
        self._calculate_direct(crop)
        self._calculate_indirect(crop)

    def _calculate_direct(self, crop: FarmedCrop):
        pass

    def _calculate_indirect(self, crop: FarmedCrop):
        pass
