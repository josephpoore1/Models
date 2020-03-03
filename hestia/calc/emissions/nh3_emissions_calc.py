from hestia.models.farmed_crop import FarmedCrop
from hestia.models.emissions.chemical.nh3_emissions import NH3Emission
from hestia.models.coefficients.conversions import Conversions
from hestia.models.geospatial.weather import Weather
from hestia.models.geospatial.soil import Soil
from hestia.data_client.data_client import DataClient


class NH3EmissionsCalc:
    def __init__(self):
        self._data_client = DataClient()

    def _calculate_for(self, crop: FarmedCrop):
        conversions = self._get_conversions(crop)
        instance = NH3Emission(conversions)
        nh3_from_synt_fert = self._get_nh3_from_synth_fert(crop.field.land.soil,
                                                           crop.field.land.weather,
                                                           conversions.fertilizer.nh3_from_synth_fert)

        instance.calculate_synthetic(crop.activities.fertilizing.synthetic.n_amount,
                                     crop.activities.fertilizing.synthetic.composition,
                                     nh3_from_synt_fert)

        instance.calculate_organic(crop.activities.fertilizing.organic.tan_amount,
                                   crop.activities.fertilizing.organic.tan_composition)

        instance.calculate_excreta(crop.activities.fertilizing.excreta.tan_amount)
        instance.calculate_excreta(crop.activities.fertilizing.excreta.tan_amount)
        instance.calculate_residue_burn(crop.activities.residue_management.crop_residue.burnt_kg)
        instance.calculate_residue(crop.activities.residue_management.crop_residue.total)

    def _get_conversions(self, crop):
        c = Conversions()
        data = self._data_client.get_lookup_data()
        c.fertilizer.nh3_from_synth_fert = data['List_NH3_Em_From_Min_Fert_Appl']
        c.fertilizer.comp_global = data['Table_FertComp_Global']
        c.fertilizer.organic.nh3_tan = data['Table_OrgFert_TAN_NH3']
        c.fertilizer.excreta.nh3_tan = data['Table_ExcrNH3_Animal']
        c.residue.n_content_ag = data['List_CRes_N_AG']
        c.residue_burn.emissions.nh3 = data['EF_Burn_DM_NH3']
        c.atomic_weights.nh3n_nh3 = data['Conv_Mol_NH3N_NH3']
        return c

    def _get_nh3_from_synth_fert(self, soil: Soil, weather: Weather, data_table):
        row_number = (0 if soil.phH20 <= 7 else 2) \
                     + (1 if weather.average_temperature < 14.5 else 2 if weather.average_temperature < 25.5 else 3)

        return data_table[row_number]