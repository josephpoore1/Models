from dataclasses import dataclass
from crops.crop_residue import CropResidue

@dataclass
class ResidueManagement: 
    crop_residue: CropResidue
