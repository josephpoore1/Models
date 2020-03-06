from hestia.models.object_model import ObjectModel
from hestia.models.crops.crop_characteristics import CropCharacteristics
from hestia.models.crops.crop_composition import CropComposition
from hestia.models.crops.crop_productivity import CropProductivity


class Crop(ObjectModel):
    characteristics: CropCharacteristics
    composition: CropComposition
    productivity: CropProductivity

    def __init__(self):
        super().__init__()