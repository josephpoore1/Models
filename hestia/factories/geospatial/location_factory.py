from hestia.models.geospatial.location import Location
from hestia.models.geospatial.location_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory
from hestia.factories.geospatial.position_factory import PositionFactory

import numpy as np
import pandas as pd

numeric_columns = ['slope', 'slope_length']


class LocationFactory(ModelFactory):
    '''Creates location instances from different data sources'''

    def __init__(self, position_factory: PositionFactory):
        self._position_factory = position_factory
        super().__init__()

    def create(self, key):
        data = self._get_record(key)
        instance = Location()
        instance.slope = data['slope']
        instance.slope_len = data['slope_length']
        self._set_position(instance, key)

        return instance

    def _set_position(self, instance, key):
        position = self._position_factory.create(key)
        instance.position = position

    def _get_record(self, key):
        df = self._data_frame
        if df is None:
            df = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'],
                                        numeric_columns)
        return data_table.loc[key]

    def _gapfill(self, data_frame):
        pass