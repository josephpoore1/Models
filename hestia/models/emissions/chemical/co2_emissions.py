from hestia.models.references.repository import ReferencesRepository
from hestia.models.farmed_crop import FarmedCrop


class CO2Emissions:
    urea: float
    lime: float

    def __init__(self, references_repository: ReferencesRepository):
        self._references = references_repository

    def calculate_for(self, crop: FarmedCrop):
        instance = CO2Emissions(self._references)
        self._calculate_lime(crop)
        self._calculate_urea(crop)

        return instance

    def _calculate_lime(self, crop: FarmedCrop):
        co2_factors = self._references.get_co2_from_urea_and_lime()

        self.lime = crop.activities.fertilizing.lime * co2_factors['lime'] + \
                    crop.activities.fertilizing.dolomite * co2_factors['dolomite']

    def _calculate_urea(self, crop: FarmedCrop):
        co2_factors = self._references.get_co2_from_urea_and_lime()
        synt_fert_nutrient = self._references.get_synth_fertilizer_nutrient_composition()

        self.urea = crop.activities.fertilizing.synthetic.n *\
                    (crop.activities.fertilizing.synthetic.composition.UREA_UAS + crop.activities.fertilizing.synthetic.composition.UAN_SOLU * synt_fert_nutrient['urea'] )* \
                    co2_factors['urea']

