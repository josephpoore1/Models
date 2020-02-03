from dataclasses import dataclass
from ..measures.energy import Energy

class Irrigation:
    technique = str
    total_water_applied = float
    energy_use = list()
    
    def addEnergyUse(self, energy):
        self.energy_use.append(energy)

    def getDiselEnergyAmount(self):
        if len(self.energy_use) < 1 :
            return Energy.Disel(0) # calculate  actual by formula
        else :
           disel_energy =[ x.amount() for x in  x.self.energy_use if x.energy_type() == "Disel"]
           return sum(disel_energy)

    def getElectricEnergyAmount(self):
        if self.energy_use is None or len(self.energy_use) < 1:
            return Energy.Disel(0) # calculate by formula
        else :
           disel_energy =[ x.amount() for x in  x.self._energyUseList if x.energy_type() == "Electricity"]
           return sum(disel_energy)
