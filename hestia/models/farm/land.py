from hestia.models.object_model import ObjectModel
from hestia.models.geospatial.weather import Weather
from hestia.models.geospatial.soil import Soil
from hestia.models.geospatial.location import Location


class Land(ObjectModel):
    area: float
    sp: str
    country: str
    geography: str
    location: Location
    soil: Soil
    weather: Weather

    def __init__(self):
        super().__init__()
