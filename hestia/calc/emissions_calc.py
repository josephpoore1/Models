from hestia.crop_builder import FarmedCropBuilder
from hestia.calc.emissions.n2o_emissions_calc import N2OEmissionsCalculator

if __name__ == '__main__':
    builder = FarmedCropBuilder()
    crop = builder.build_crop(20)

    calc = N2OEmissionsCalculator()
    calc.calculate_for(crop)