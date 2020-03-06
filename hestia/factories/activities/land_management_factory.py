from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.tillage_management import TillageManagement
from hestia.models.activities.irrigation.irrigation_mapping import MODEL_MAPPING

import numpy as np


class LandManagementFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data = self._data_frame
        if data is None:
            data = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._gapfill(data_table)
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        data_fame.replace('-', np.NAN, inplace=True)

    def create(self, key):
        record = self._get_record(key)
        instance = TillageManagement()
        instance.method = record['method']

        return instance
