from hestia.models.farmed_crop import FarmedCrop
from hestia.models.references.repository import ReferencesRepository


class MachineryAndInfrastructureProductionEmissions:
    co2: float
    so2: float
    po4: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references = references_repository

    def _calculate_for(self,crop: FarmedCrop):
        self._calculate_so2(crop)
        self._calculate_co2(crop)
        self._calculate_po4(crop)

    def _calculate_co2(self, crop: FarmedCrop):
        pass

    def _calculate_so2(self, crop: FarmedCrop):
        pass

    def _calculate_po4(self, crop: FarmedCrop):
        pass