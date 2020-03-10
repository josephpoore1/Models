from hestia.models.farm.machinery.machinery import Machinery
from hestia.models.farm.machinery.machinery_mapping import MODEL_MAPPING
from hestia.models.measures.energy import Energy
from hestia.factories.model_factory import ModelFactory

numeric_columns =['amount','fuel_amount', 'hours']


class MachineryFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def create(self, key):
        data = self._get_record(key)
        instance = Machinery()
        return self._map(instance, data)

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'],
                                        numeric_columns)
        return data_table.loc[key]

    def _map(self, instance: Machinery, data):
        instance.energy = Energy(data['fuel_amount'], 0)
        instance.amount = data['amount']
        instance.hours = data['hours']
        return instance

    def _gapfill(self, data_frame):
        pass
