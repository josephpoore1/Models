from hestia.models.object_model import ObjectModel


class Country(ObjectModel):
    name: str

    def __init__(self):
        super().__init__()
