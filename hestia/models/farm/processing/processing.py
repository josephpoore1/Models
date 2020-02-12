from dataclasses import dataclass
from hestia.models.measures.energy import Energy

@dataclass
class Processing:
    drying_grading: Energy