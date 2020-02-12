from dataclasses import dataclass
from hestia.models.crops.crop_characteristics import CropCharacteristics
from hestia.models.crops.crop_composition import CropComposition
from hestia.models.crops.crop_productivity import CropProductivity

@dataclass
class Crop:
    characteristics: CropCharacteristics
    composition: CropComposition
    productivity: CropProductivity
