from hestia.data_client.file_readers.json_reader import JsonReader
import pandas as pd


class DataClient:
    def __init__(self):
        pass

    def get_data_frame(self, configuration):
        from_file = configuration['location']
        use_columns = configuration['column_names']
        location_type = configuration['location_type']

        if location_type == 'directory':
            return self.get_lookup_data(from_file, use_columns)
        if location_type == 'file':
            column_delimiter = configuration['separator']
            return self.get_observations_data(from_file, column_delimiter, use_columns)

        raise Exception('location_type is not supported')

    def get_observations_data(self, from_file, delimiter, columns=None):
        return pd.read_csv(from_file, delimiter= delimiter, usecols=columns)

    def get_lookup_data(self, lookup_data_source, columns):
        json_reader = JsonReader(lookup_data_source)
        data = json_reader.read(**columns)
        return data
