from hestia.models.object_model import ObjectModel
from hestia.models.geospatial.eco_climate_zone import EcoClimateZone


class Weather(ObjectModel):
    precipitation: float
    average_temperature: float
    winter_type_corr: int
    pet: float
    eco_clim_zone: EcoClimateZone

    def __init__(self):
        super().__init__()
