from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.fertilizers.excreta.excreta import Excreta
from hestia.models.activities.fertilizers.excreta.excreta_mapping import MODEL_MAPPING

import numpy as np


class ExcretaFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._gapfill(data_table)
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        data_fame.replace('-', np.NAN, inplace=True)

    def create(self, key):
        record = self._get_record(key)
        instance = Excreta()
        self._map(instance, record)
        return instance

    def _map(self, instance: Excreta, data):
        instance.n_amount = data['n_amount']
        instance.tan_amount = data['tan_amount']
        instance.animal = data['animal']
