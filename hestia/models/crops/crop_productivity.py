from hestia.models.object_model import ObjectModel


class CropProductivity(ObjectModel):
    nursery_duration: float
    sapling_yield: float
    cultiv_duration: float
    orch_density: float
    fallow_duration : float
    non_bear_duration: float

    def __init__(self):
        super().__init__()
