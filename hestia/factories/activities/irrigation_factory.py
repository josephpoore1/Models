from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.irrigation.irrigation import Irrigation
from hestia.models.activities.irrigation.irrigation_mapping import MODEL_MAPPING
from hestia.models.measures.energy import Energy

numeric_columns = ['amount_applied',
                   'energy_fuel',
                   'energy_electr']


class IrrigationFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data = self._data_frame
        if data is None:
            data = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'],
                                        numeric_columns)
        return data_table.loc[key]

    def _gapfill(self, data_frame):
        pass

    def create(self, key):
        record = self._get_record(key)
        energy = Energy(record['energy_fuel'], record['energy_electr'])
        irrigation = Irrigation()
        irrigation.energy = energy
        irrigation.applied_amount = record['amount_applied']
        irrigation.type = record['type']

        return irrigation
