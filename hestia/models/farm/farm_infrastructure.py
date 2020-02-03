from dataclasses import dataclass
from ..measures.energy import Energy

@dataclass
class MachineryAndInfrastructure:
    energy: Energy
    amount: float
    hours: float
    plastic: float
