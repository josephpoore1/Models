from dataclasses import dataclass

@dataclass
class CropResidue:
    removed_amount: float
    burnt_amount: float
    above_ground_remaining_amount: float
    below_ground_remaining_amount: float
    total_amount: float
