from dataclasses import dataclass
from hestia.models.measures.energy import Energy

@dataclass
class CropProcessing:
    drying_grading: Energy