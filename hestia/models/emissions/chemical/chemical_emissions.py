from dataclasses import dataclass

from ch4_emissions import CH4Emission
from co2_emissions import CO2Emissions
from n2o_emissions import N2OEmission
from no3_emissions import NO3Emission
from nox_emissions import NOxEmission
from nh3_emissions import NH3Emission
from p_emissions import PhosphorusEmissions

@dataclass
class ChemicalEmissions:
    ch4: CH4Emission
    co2: CO2Emissions
    no2: N2OEmission
    nox: NOxEmission
    no3: NO3Emission
    nh3: NH3Emission
    p: PhosphorusEmissions