from abc import ABC, abstractmethod
from hestia.data_client.file_readers.json_reader import JsonReader
import pandas as pd


class ModelFactory(ABC):
    def __init__(self):
        self._data_frame = None

    @abstractmethod
    def _get_record(self, key):
        pass

    @abstractmethod
    def _gapfill(self, data_fame):
        '''Replaces missing (NaN) values with a proposed ones'''
        return data_fame

    @abstractmethod
    def create(self, key):
        pass

    # @property
    # def data_frame(self):
    #     return self._data_frame

    def set_data_frame(self, data_frame):
        self._data_frame = data_frame

    def _get_data_frame(self, configuration):
        from_file = configuration['location']
        use_columns = configuration['column_names']
        location_type = configuration['location_type']

        if location_type == 'directory':
            return self._get_lookup_data(from_file, use_columns)
        if location_type == 'file':
            column_delimiter = configuration['separator']
            return self._get_observations_data(from_file, column_delimiter, use_columns)

        raise Exception('location_type is not supported')

    def _get_observations_data(self, from_file, delimiter, columns=None):
        return pd.read_csv(from_file, delimiter= delimiter, usecols=columns)

    def _create_table(self, data_frame, columns, index_key):
        data_frame = data_frame.rename(columns=columns).set_index(index_key, drop=False)
        return pd.DataFrame(data_frame)

    def _get_lookup_data(self, lookup_data_source, columns):
        json_reader = JsonReader(lookup_data_source)
        data = json_reader.read(**columns)
        return pd.DataFrame(data)

    def _convert(self, data_frame, column_mappings):
        '''Converts values in columns to a proposed type'''
        return data_frame

    def _map(self, instance, data, props):
        for item in props:
            instance.__setattr__(item, data[item])
        return instance