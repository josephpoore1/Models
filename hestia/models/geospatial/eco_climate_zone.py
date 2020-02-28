from hestia.models.object_model import ObjectModel


class EcoClimateZone(ObjectModel):
    name: str
    value: int
    c_class: str
    c_nox_N: float
    c_n2o_N: float

    def __init__(self):
        super().__init__()