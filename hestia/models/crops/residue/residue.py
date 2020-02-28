from hestia.models.object_model import ObjectModel


class CropResidue(ObjectModel):
    removed: float
    burnt_percent: float
    burnt_kg: float
    above_ground_remaining: float
    below_ground_remaining: float
    total: float

    def __init__(self):
        super().__init__()
