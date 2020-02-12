from dataclasses import dataclass
from hestia.models.measures.energy import Energy

@dataclass()
class Machinery:
    hours: float
    amount: float
    energy: Energy