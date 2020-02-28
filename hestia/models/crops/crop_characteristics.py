from hestia.models.object_model import ObjectModel


class CropCharacteristics(ObjectModel):
    crop_name : str
    crop_type: str
    crop_root_depth: float

    def __init__(self):
        super().__init__()
