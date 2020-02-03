from dataclasses import dataclass

@dataclass
class NH3Emission:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    residue_burn: float
    total: float