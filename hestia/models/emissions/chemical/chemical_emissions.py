from hestia.models.emissions.chemical.ch4_emissions import CH4Emission
from hestia.models.emissions.chemical.co2_emissions import CO2Emissions
from hestia.models.emissions.chemical.n2o_emissions import N2OEmission
from hestia.models.emissions.chemical.no3_emissions import NO3Emission
from hestia.models.emissions.chemical.nox_emissions import NOxEmission
from hestia.models.emissions.chemical.nh3_emissions import NH3Emission
from hestia.models.emissions.chemical.p_emissions import PhosphorusEmissions


class ChemicalEmissions:
    ch4: CH4Emission
    co2: CO2Emissions
    no2: N2OEmission
    nox: NOxEmission
    no3: NO3Emission
    nh3: NH3Emission
    p: PhosphorusEmissions

    def __init__(self):
        pass