from hestia.models.farmed_crop import FarmedCrop
from hestia.models.references.repository import ReferencesRepository
import numpy as np


class PhosphorusEmissions:
    R: float
    P: float
    A: float
    Pe: float
    Pr: float
    Pd: float
    Pg: float
    PToWater: float
    NErosion: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references =references_repository

    def calculate_for(self, crop:FarmedCrop):
        self.calculate_p(crop)
        self.calculate_Pd(crop)
        self.calculate_Pg(crop)
        self.calculate_Pr(crop)
        self.calculate_r(crop)

        self.calculate_a(crop, self.R, self.P)
        self.calculate_n_erosion(crop, self.A)
        self.calculate_Pe(crop, self.A)
        self.calculate_p_to_water(self.Pe, self.Pd, self.Pg, self.Pr)

    def calculate_r(self, crop: FarmedCrop):
        if crop.field.land.weather.winter_type_corr is None or crop.field.land.weather.precipitation is None or crop.activities.irrigation.applied_amount is None:
            self.R = None
            # and log warning here
        else:
            if (crop.field.land.weather.winter_type_corr * crop.activities.irrigation.applied_amount / 10 + crop.field.land.weather.precipitation) > 850:
                self.R = 578.8 - 1.219 * (crop.activities.irrigation.applied_amount / 10 + crop.field.land.weather.precipitation) + 0.004105 * \
                         pow(crop.activities.irrigation.applied_amount / 10 + crop.field.land.weather.precipitation, 2) * crop.field.land.weather.winter_type_corr
            else:
                self.R = 0.0483 * (crop.activities.irrigation.applied_amount / 10 +
                                   pow(crop.field.land.weather.precipitation, 1.61)) * crop.field.land.weather.winter_type_corr

    def calculate_p(self, crop: FarmedCrop):
        spatial_p_practice = self._references.get_spatial_p_practices()
        self.P = spatial_p_practice.loc[crop.field.land.country]

    def calculate_a(self, crop: FarmedCrop, r, p):
        c1_crop_factors = self._references.get_p_loss_c1_factors_crop()
        c2_country_factors = self._references.get_p_loss_c2_factors_ctry()
        c2_tillage_factors = self._references.get_p_loos_c2_factors_tillage()
        p_correction = self._references.get_correction_for_practice_factor()

        self.A = r * crop.field.land.soil.erodibility * crop.field.land.location.slope_len * \
                 c1_crop_factors.loc[crop.crop.characteristics.crop_name] * \
                 c2_country_factors.loc[crop.field.land.country] if (crop.crop.characteristics.crop_name == 'Pasture' or crop.activities.residue_management.method == '-') else \
            c2_tillage_factors.loc[crop.activities.residue_management.method] * \
            p * p_correction.loc[lambda df: df['Pcorr'] == crop.field.land.location.slope, 'Pcorr']

    def calculate_Pe(self, crop: FarmedCrop, a):
        self.Pe = a * crop.field.land.soil.loss_to_auqatics * 2 * crop.field.land.soil.phosphorus

    def calculate_Pr(self, crop: FarmedCrop):
        self.Pr = \
            (0 if crop.field.land.location.slope < 0.03 else 1) * \
            (1 + 0.2/80 * crop.activities.fertilizing.synthetic.p + 0.7/80 *crop.activities.fertilizing.organic.p *
             (0 if crop.activities.fertilizing.organic.n_composition.liquid_or_slurry is None else crop.activities.fertilizing.organic.n_composition.liquid_or_slurry) +
            0.4/80 * (crop.activities.fertilizing.organic.p * sum(crop.activities.fertilizing.organic.n_composition.to_series()) + crop.activities.fertilizing.excreta.p))

    def calculate_Pd(self, crop: FarmedCrop):
        self.Pd = 0.07 * \
                  (1 +
                   (0 if crop.activities.fertilizing.organic.p == 0
                    else (0.2 / 80 * crop.activities.fertilizing.organic.p *
                          (0 if crop.activities.fertilizing.organic.n_composition.liquid_or_slurry is None else crop.activities.fertilizing.organic.n_composition.liquid_or_slurry)))) * \
                  (6 if crop.field.land.soil.drainage_class > 3 else 0)

    def calculate_Pg(self, crop: FarmedCrop):
        self.Pg = 0.07 * \
                  (1 +
                   (0 if crop.activities.fertilizing.organic.p == 0
                    else (0.2 / 80 * crop.activities.fertilizing.organic.p *
                          (0 if crop.activities.fertilizing.organic.n_composition.liquid_or_slurry is None else crop.activities.fertilizing.organic.n_composition.liquid_or_slurry)))) * \
                  (0 if crop.field.land.soil.drainage_class > 3 else 1)


    def calculate_p_to_water(self, Pe, Pd, Pg, Pr):
        self.PToWater = Pe + Pd + Pg + Pr

    def calculate_n_erosion(self, crop: FarmedCrop, a):
        self.NErosion = a * crop.field.land.soil.loss_to_auqatics * 2 * crop.field.land.soil.nitrogen

