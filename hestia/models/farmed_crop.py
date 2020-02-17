from hestia.models.activities.farm_activities import FarmActivities
from hestia.models.crops.crop import Crop
from hestia.models.farm.farm_infrastructure import FarmInfrastructure
from hestia.models.farm.field import Field

from hestia.models.measures.crop_yield import CropYield


class FarmedCrop:
    seed: float
    crop_yield: CropYield
    farming_period: int
    crop: Crop
    field: Field
    activities: FarmActivities
    infrastructure: FarmInfrastructure
