from hestia.data_client.file_readers.json_reader import JsonReader

import pandas as pd

class ObservationsFactory:
    def __init__(self):
        self._data_frame

    def set_data_frame(self, data_frame):
        self._data_frame = data_frame

    def _get_observations_data(self, from_file, delimiter, columns):
        return pd.read_csv(from_file, delimiter= delimiter, usecols=columns)

    def _get_lookup_data(self, lookup_data_source, column_mappings):
        json_reader = JsonReader(lookup_data_source)
        data = json_reader.read(**column_mappings)
        return pd.DataFrame(data)
