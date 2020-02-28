from hestia.models.object_model import ObjectModel


class CropComposition(ObjectModel):
    gross_energy: float
    nitrogen_amount: float
    dm_at_harvest: float
    dm_marketable: float

    def __init__(self):
        super().__init__()
