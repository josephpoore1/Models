from dataclasses import dataclass
from datetime import timedelta
from Activities import FarmActivities
from Crops import Crop
from Farm import Farm, LandUseManagemet

@dataclass
class FarmedCrop:
    crop: Crop
    farm: Farm
    farming_period: timedelta
    seed_amount: float
    crop_yield_amount: float
    _farm_activities : FarmActivities
    _land_use: LandUseManagemet


    def addFertilizer(self, fertilizer):
        self._farm_activities.addFertilizer(fertilizer)

    def addIriigation(self, amount, irrig_type):
        self._farm_activities.addIrrigation(irrig_type, amount)

    def list_activities(self):
        return self._farm_activities.toList()
