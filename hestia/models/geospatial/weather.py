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

    def get_average_temp_index(self):
        return \
            'cool' if self.average_temperature <= 14 else \
            'temperate' if (self.average_temperature > 15 and self.average_temperature < 25) else \
            'warm'