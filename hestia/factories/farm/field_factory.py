from hestia.models.farm.field import Field
from hestia.models.farm.field_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory
from hestia.factories.farm.land_factory import LandFactory

import numpy as np


class FieldFactory(ModelFactory):
    def __init__(self, land_factory: LandFactory):
        super().__init__()
        self._land_factory = land_factory

    def create(self, key):
        data = self._get_record(key)
        instance = Field()
        self._set_land(data, key)
        return self._map(data, instance)

    def _set_land(self, instance, key):
        instance.land = self._land_factory.create(key)

    def _map(self, data, instance: Field):
        instance.id = data['id']
        return instance

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

