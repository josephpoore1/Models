from dataclasses import dataclass

@dataclass
class NOxEmission:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float
    total: float