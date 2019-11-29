from dataclasses import dataclass
from Crops import CropCharacteristics as Characteristics, CropComposition as Composition, CropProductivity as Productivity

@dataclass
class Crop:
    characteristics: Characteristics
    composition: Composition
    productivity: Productivity
    
