from hestia.models.object_model import ObjectModel


class TillageManagement(ObjectModel):
    method: str

    def __init__(self):
        super().__init__()