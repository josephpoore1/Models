from dataclasses import dataclass
from hestia.models.measures.energy import Energy


@dataclass
class Irrigation:
    type: str
    applied_amount: float
    energy: Energy
