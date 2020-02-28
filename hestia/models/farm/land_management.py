from hestia.models.object_model import ObjectModel


class LandManagement(ObjectModel):
    cultivation_duration: int
    crop_allocation: float
    fallow_allocation: float

    def __init__(self):
        super().__init__()
