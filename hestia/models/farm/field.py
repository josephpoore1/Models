from dataclasses import dataclass
from ..geospatial import Land

@dataclass
class Field:
    machinery: list
    infrastructure: list
    land: Land
    lime_amount: float
    dolomite_amount: float
    
    def addLime(self, amount):
        self.lime_amount  += amount
    
    def addDolomite(self, amount):
        self.dolomite_amount += amount
    
    def addMachinery(self, machinery):
        self.machinery.append(machinery)
    
    def addInfrastructure(self, machinery):
        self.machinery.append(machinery)