from hestia.models.geospatial.eco_climate_zone import EcoClimateZone

class Weather:
    precipitation: float
    average_temperature: float
    winter_type_corr: int
    pet: float
    eco_clim_zone: EcoClimateZone
