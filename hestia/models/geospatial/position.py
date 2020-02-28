from hestia.models.object_model import ObjectModel


class Position(ObjectModel):
    def __init__(self):
        super().__init__()

    lat: float
    lon: float
