from dataclasses import dataclass
from Geospatial import EcoClimateZone

class Weather:
    precipitation: float
    average_temperature: float
    winter_type_corr: int
    pet: float
    eco_clim_zone: EcoClimateZone
    
