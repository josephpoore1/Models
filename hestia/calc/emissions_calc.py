from hestia.crop_builder import FarmedCropBuilder

from hestia.models.emissions.chemical.nh3_emissions import NH3Emissions
from hestia.models.emissions.chemical.no3_emissions import NO3Emissions
from hestia.models.emissions.chemical.nox_emissions import NOxEmissions
from hestia.models.emissions.chemical.n2o_emissions import N2OEmissions
from hestia.models.emissions.chemical.ch4_emissions import CH4Emissions
from hestia.models.emissions.chemical.co2_emissions import CO2Emissions
from hestia.models.emissions.chemical.p_emissions import PhosphorusEmissions

from hestia.models.references.repository import ReferencesRepository

if __name__ == '__main__':
    builder = FarmedCropBuilder()
    crop = builder.build_crop(970)

    references = ReferencesRepository()

    nh3 = NH3Emissions(references)
    nox = NOxEmissions(references)
    n2o = N2OEmissions(references)
    no3 = NO3Emissions(references)
    ch4 = CH4Emissions(references)
    co2 = CO2Emissions(references)
    p_emissions = PhosphorusEmissions(references)

    p_emissions.calculate_for(crop)
    nh3.calculate_for(crop)

    n2o.calculate_for(crop)
    no3.calculate_for(crop)
    ch4.calculate_for(crop)
    co2.calculate_for(crop)