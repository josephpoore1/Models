from dataclasses import dataclass

@dataclass
class N2OEmission:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float
    total: float