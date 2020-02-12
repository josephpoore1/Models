from hestia.data_client.file_readers.json_reader import JsonReader

import pandas as pd


class ModelFactory:
    def __init__(self):
        self._data_frame = None

    # @property
    # def data_frame(self):
    #     return self._data_frame

    def set_data_frame(self, data_frame):
        self._data_frame = data_frame

    def _get_observations_data(self, from_file, delimiter, columns, index_key):
        data_frame = pd.read_csv(from_file, delimiter= delimiter, usecols=columns)
        data_frame = data_frame.rename(columns=columns).set_index(index_key)
        return pd.DataFrame(data_frame)

    def _get_lookup_data(self, lookup_data_source, column_mappings):
        json_reader = JsonReader(lookup_data_source)
        data = json_reader.read(**column_mappings)
        return pd.DataFrame(data)

    def _map(self, instance, data, props):
        for item in props:
            instance.__setattr__(item, data[item])
        return instance