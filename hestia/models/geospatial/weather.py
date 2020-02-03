from dataclasses import dataclass
from ecoclimate_zone import EcoClimateZone

class Weather:
    precipitation: float
    average_temperature: float
    winter_type_corr: int
    pet: float
    eco_clim_zone: EcoClimateZone
    
