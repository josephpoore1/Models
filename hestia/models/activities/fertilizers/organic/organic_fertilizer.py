from dataclasses import dataclass
from .organic_fertilizer_composition import OrganicFertilizerComposition


@dataclass
class OrganicFertilizer:
    n_amount: float
    tan_amount: float
    p_amount: float
    k_amount: float
    n_composition: OrganicFertilizerComposition
    tan_composition: OrganicFertilizerComposition
