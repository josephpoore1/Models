from dataclasses import dataclass

from activities.farm_activities import FarmActivities
from crops.crop import Crop
from crops.crop_infrastructure import CropInfrastructure
from farm.field import Field
from farm.farm_infrastructure import MachineryAndInfrastructure
from measures.crop_yield import CropYield

@dataclass
class FarmedCrop:
    seed: float
    crop_yield: CropYield
    farming_time: int
    crop: Crop
    field: Field
    activities: FarmActivities
    infrastructure: CropInfrastructure
    machinery: MachineryAndInfrastructure
