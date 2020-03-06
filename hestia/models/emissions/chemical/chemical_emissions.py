from hestia.models.emissions.chemical.ch4_emissions import CH4Emissions
from hestia.models.emissions.chemical.co2_emissions import CO2Emissions
from hestia.models.emissions.chemical.n2o_emissions import N2OEmissions
from hestia.models.emissions.chemical.no3_emissions import NO3Emissions
from hestia.models.emissions.chemical.nox_emissions import NOxEmissions
from hestia.models.emissions.chemical.nh3_emissions import NH3Emissions
from hestia.models.emissions.chemical.p_emissions import PhosphorusEmissions
from hestia.models.farmed_crop import FarmedCrop
from hestia.models.references.repository import ReferencesRepository

class ChemicalEmissions:
    ch4: CH4Emissions
    co2: CO2Emissions
    no2: N2OEmissions
    nox: NOxEmissions
    no3: NO3Emissions
    nh3: NH3Emissions
    p: PhosphorusEmissions

    def __init__(self):
        self._references = ReferencesRepository()

    def create_for(self, crop: FarmedCrop):
        instance = ChemicalEmissions()

        instance.ch4 = CH4Emissions(self._references)\
            .calculate_for(crop)
        instance.co2 = CO2Emissions(self._references)\
            .calculate_for(crop)
        instance.no2 = N2OEmissions(self._references)\
            .calculate_for(crop)
        instance.nox = NOxEmissions(self._references)\
            .calculate_for(crop)
        instance.no3 = NO3Emissions(self._references)\
            .calculate_for(crop)
        instance.nh3 = NH3Emissions(self._references)\
            .calculate_for(crop)
        instance.p = PhosphorusEmissions(self._references)\
            .calculate_for(crop)
        return instance