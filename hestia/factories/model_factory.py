from abc import ABC, abstractmethod
from hestia.data_client.data_client import DataClient
from hestia.models.references.repository import ReferencesRepository
import pandas as pd
import numpy as np


class ModelFactory(ABC):
    def __init__(self):
        self._data_frame = None
        self._data_client = DataClient()
        self._references = ReferencesRepository()

    @abstractmethod
    def _get_record(self, key):
        pass

    @abstractmethod
    def _gapfill(self, data_frame):
        '''Replaces missing (NaN) values with a proposed ones'''
        return data_frame

    @abstractmethod
    def create(self, key):
        pass

    def set_data_frame(self, data_frame):
        self._data_frame = data_frame

    def _get_data_frame(self, configuration):
        return self._data_client.get_data_frame(configuration)

    def _get_observations_data(self, from_file, delimiter, columns=None):
        return self._get_observations_data(from_file,delimiter)

    def _create_table(self, data_frame, columns, index_key, numeric_columns=[]):
        data_frame = data_frame.rename(columns=columns).set_index(index_key, drop=False)
        data_frame[numeric_columns] = data_frame[numeric_columns].apply(pd.to_numeric, errors='coerce')
        data_frame.replace('-', np.NAN, inplace=True)

        return pd.DataFrame(data_frame)

    def _get_lookup_data(self, lookup_data_source, columns):
        data = self._data_client.get_lookup_data(lookup_data_source,columns)
        return pd.DataFrame(data)

    def _convert(self, data_frame, column_mappings):
        '''Converts values in columns to a proposed type'''
        return data_frame

    def _map(self, instance, data, props):
        for item in props:
            instance.__setattr__(item, data[item])
        return instance