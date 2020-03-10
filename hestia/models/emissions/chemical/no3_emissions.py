from hestia.models.farmed_crop import FarmedCrop
from hestia.models.crops.crop_characteristics import CropCharacteristics
from hestia.models.geospatial.weather import Weather
from hestia.models.geospatial.soil import Soil
from hestia.models.farm.land import Land
from hestia.models.references.repository import ReferencesRepository


import numpy as np


class NO3Emissions:
    synthetic: float
    organic: float
    excreta: float
    residue: float
    total: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references = references_repository

    def calculate_for(self, crop: FarmedCrop):
        self.calculate_total(crop)

        self.calclulate_excreta(crop, self.total)
        self.calclulate_synthetic(crop, self.total)
        self.calclulate_organic(crop, self.total)
        self.calclulate_residue(crop, self.total)

    def calclulate_organic(self, crop: FarmedCrop, no3_total):
        self.organic= no3_total *  crop.activities.fertilizing.organic.n /  self._get_total_n(crop)

    def calclulate_synthetic(self, crop: FarmedCrop, no3_total):
        self.synthetic= no3_total *  crop.activities.fertilizing.synthetic.n / self._get_total_n(crop)

    def calclulate_excreta(self, crop: FarmedCrop, no3_total):
        self.excreta= no3_total *  crop.activities.fertilizing.excreta.n / self._get_total_n(crop)

    def calclulate_residue(self, crop: FarmedCrop, no3_total):
        self.residue= no3_total *  crop.activities.residue_management.crop_residue.total /  self._get_total_n(crop)

    def calculate_total(self, crop: FarmedCrop):
        atomic_weights = self._references.get_atomic_weight_conversions()
        self.total = self._get_total_n(crop) \
                     * self._get_leaching_factor(crop=crop.crop.characteristics,
                                                 soil=crop.field.land.soil,
                                                 weather=crop.field.land.weather,
                                                 land=crop.field.land) \
                     * atomic_weights['no3n_no3']

    def _get_leaching_factor(self, crop: CropCharacteristics, soil: Soil, weather: Weather, land: Land):
        leaching = self._references.get_no3_leaching()
        if land.sp == 'A' or land.sp == '-':
            return leaching['other']
        elif (crop.crop_root_depth > 1.3 or soil.clay > 0.50 or weather.precipitation < 500 ) and (crop.crop_root_depth > 0.4 or soil.sand < 0.85 or weather.precipitation < 1300):
            return leaching['low']
        elif (crop.crop_root_depth < 0.4 or soil.sand > 0.85 or weather.precipitation > 1300 ) and (crop.crop_root_depth > 1.3 or soil.clay < 0.5 or weather.precipitation > 500):
            return leaching['high']
        else:
            return leaching['other']

    def _get_total_n(self, crop: FarmedCrop):
        return sum(
            (crop.activities.fertilizing.organic.n,
             crop.activities.fertilizing.synthetic.n,
             crop.activities.fertilizing.excreta.n,
             crop.activities.residue_management.crop_residue.total))