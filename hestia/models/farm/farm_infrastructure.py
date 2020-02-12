from dataclasses import dataclass
from hestia.models.farm.machinery.machinery import Machinery
from hestia.models.farm.irrigation.irrigation import Irrigation
from hestia.models.farm.processing.processing import Processing


@dataclass
class FarmInfrastructure:
    machinery: Machinery
    irrigation: Irrigation
    processing: Processing
    plastic: float
