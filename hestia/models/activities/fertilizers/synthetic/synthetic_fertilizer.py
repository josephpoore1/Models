from dataclasses import dataclass
from ..fertilizer import Fertilizer


@dataclass
class SyntheticFertilizer(Fertilizer):
    name: str
    amount: float
    chemical_formula: str
    fertilizer_type = "Synthetic"