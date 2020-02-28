from hestia.models.farmed_crop import FarmedCrop
from hestia.models.emissions.chemical.n2o_emissions import N2OEmissions
from hestia.data_client.data_client import DataClient
from hestia.models.emissions.chemical.n2o_emissions_mapping import MODEL_MAPPING
from hestia.models.coefficients.conversions import Conversions


class N2OEmissionsCalculator:
    def __init__(self):
        self._data_client = DataClient()

    def calculate_for(self, crop: FarmedCrop):
        conversions = self._get_conversions(crop)
        instance = N2OEmissions(conversions)

        instance.calculate_n2o_total(crop.activities.fertilizing, crop.field.land.soil)
        instance.calculate_organic(crop.activities.fertilizing.organic.n_amount, crop.activities.fertilizing.total_n())
        instance.calculate_synthetic(crop.activities.fertilizing.synthetic.n_amount, crop.activities.fertilizing.total_n())
        instance.calculate_excreta(crop.activities.fertilizing.excreta.n_amount, crop.activities.fertilizing.total_n())
        instance.calculate_residue(crop.activities.residue_management.crop_residue.total)
        instance.calculate_residue_burn(crop.activities.residue_management.crop_residue.burnt_kg)

        return instance


    def _get_conversions(self, crop):
        data = self._data_client.get_data_frame(MODEL_MAPPING)
        conversions = Conversions()

        # ToDo: Probably the right way would be toadd metadata to these values
        # use pandas to create a dataframes
        conversions.crop.emissions.c_n2o_N = data["c_n2on_crop_emission"]
        conversions.climate.c_n2o_n_climate = data["c_n2o_n_climate"]
        conversions.atomic_weights.c_n2on_weight_conversion = data["c_n2on_weight_conversion"]

        return conversions