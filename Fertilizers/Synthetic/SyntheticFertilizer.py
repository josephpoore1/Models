from dataclasses import dataclass
from Fertilizers.Fertilizer import Fertilizer

@dataclass
class SyntheticFertilizer(Fertilizer):
    name: str
    amount: float
    chemical_formla: str
    fetilizer_type = "Synthetic"