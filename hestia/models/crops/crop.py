from hestia.models.crops.crop_characteristics import CropCharacteristics
from hestia.models.crops.crop_composition import CropComposition
from hestia.models.crops.crop_productivity import CropProductivity


class Crop:
    characteristics: CropCharacteristics
    composition: CropComposition
    productivity: CropProductivity
