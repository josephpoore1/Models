from json_reader import JsonReader
from csv_reader import CSVReader

class ReaderFactory:
    def __init__(self):
        pass

    def create_reader(self, source_type, data_type, **kwargs):
        if source_type == 'file' & data_type == 'csv':
            return CSVReader(location= kwargs['location'], delimiter= kwargs['delimitier'])
        elif data_type == 'json':
            return JsonReader(source= kwargs['location']+kwargs['name'])
