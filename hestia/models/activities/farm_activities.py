from dataclasses import dataclass

from fertilizing import Fertilizing
from irrigation import Irrigation
from pesticide_management import PesticideManagement
 
@dataclass
class FarmActivities:
    fertilizing: Fertilizing
    irrigation: Irrigation
    pests: PesticideManagement

    def addFertilizer(self, fertilizer):
        if self.fertilizing is None:
            self.fertilizing = Fertilizing()

        self.fertilizing.addFertilizer(fertilizer)
    
    def addIrrigation(self, irrigation):
        self.irrigation = irrigation
    