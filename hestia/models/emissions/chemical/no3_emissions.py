from dataclasses import dataclass

@dataclass
class NO3Emission:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    total: float