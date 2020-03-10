from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.fertilizers.organic.organic_fertilizer import OrganicFertilizer
from hestia.models.activities.fertilizers.organic.organic_fertilizer import OrganicFertilizerComposition
from hestia.models.activities.fertilizers.organic.organic_fertilizer_mapping import MODEL_MAPPING


class OrganicFertilizerFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'],
                                        slice(None))
        return data_table.loc[key]

    def _gapfill(self, data_frame):
        pass

    def create(self, key):
        record = self._get_record(key)

        instance = OrganicFertilizer()
        self._set_n_composition(instance, record)
        self._set_tan_composition(instance, record)
        self._map(instance, record)

        return instance

    def _map(self, instance, data):
        instance.n = data['n_amount']
        instance.tan = data['tan_amount']
        instance.p = data['p_amount']
        instance.k = data['k_amount']

    def _set_n_composition(self, instance, record):
        composition = OrganicFertilizerComposition()
        composition.compost = record['n_compost']
        composition.liquid_or_slurry = record['n_liquid']
        composition.green_manure = record['n_manure']
        composition.solid = record['n_solid']
        instance.n_composition = composition

    def _set_tan_composition(self, instance, record):
        composition = OrganicFertilizerComposition()
        composition.compost = record['tan_compost']
        composition.liquid_or_slurry = record['tan_liquid']
        composition.green_manure = record['tan_manure']
        composition.solid = record['tan_solid']
        instance.tan_composition = composition
