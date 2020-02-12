from dataclasses import dataclass

from hestia.models.activities.farm_activities import FarmActivities
from hestia.models.crops.crop import Crop

from hestia.models.farm.field import Field

from hestia.models.measures.crop_yield import CropYield

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
