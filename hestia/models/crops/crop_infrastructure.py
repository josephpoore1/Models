from dataclasses import dataclass

@dataclass
class CropInfrastructure:
    glass_and_perlite: float
    plastic: float
    rock_wool: float
    steel: float
    aluminium: float
    iron: float
    concrete: float
    wood: float