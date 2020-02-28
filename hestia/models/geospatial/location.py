from hestia.models.object_model import ObjectModel
from hestia.models.geospatial.position import Position


class Location(ObjectModel):
    position: Position
    slope: float
    slope_len: float

    def __init__(self):
        super().__init__()
