from dataclasses import dataclass

from crop_characteristics import CropCharacteristics
from crop_composition import CropComposition
from crop_productivity import CropProductivity

@dataclass
class Crop:
    characteristics: CropCharacteristics
    composition: CropComposition
    productivity: CropProductivity
    
