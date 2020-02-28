from hestia.models.object_model import ObjectModel
from hestia.models.measures.energy import Energy


class Machinery(ObjectModel):
    hours: float
    amount: float
    energy: Energy

    def __init__(self):
        super().__init__()