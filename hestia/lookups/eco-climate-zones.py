from dataclasses import dataclass

@dataclass
class EcoClimateZone:
    climate : str
    value: int
    c_class: str
    c_nox_N: float
    c_n20_N: float