import json

class JsonWriter:
    def __init__(self, destination):
        self._destination = destination

    def write(self, data, document_name):
        with open(f'{self._destination}/{document_name}.json', 'w') as file_handle:
            json.dump(data, file_handle)