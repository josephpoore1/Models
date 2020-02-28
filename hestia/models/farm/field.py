from hestia.models.object_model import ObjectModel
from hestia.models.farm.land import Land


class Field(ObjectModel):
    land: Land

    def __init__(self):
        super().__init__()
