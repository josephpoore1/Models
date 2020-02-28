from hestia.models.object_model import ObjectModel
from hestia.models.activities.farm_activities import FarmActivities
from hestia.models.crops.crop import Crop
from hestia.models.farm.farm_infrastructure import FarmInfrastructure
from hestia.models.farm.field import Field

from hestia.models.measures.crop_yield import CropYield


class FarmedCrop(ObjectModel):
    seed: float
    crop_yield: CropYield
    farming_period: int
    crop: Crop
    field: Field
    activities: FarmActivities
    infrastructure: FarmInfrastructure

    def __init__(self):
        super().__init__()
