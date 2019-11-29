from dataclasses import dataclass

@dataclass
class EcoClimZone:
    name: str
    value: str
    climate_class: str
    n2o_n_coeff: float
    nox_n_coeff: float
