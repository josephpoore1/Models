import json

class JsonLoader:

    def __init__(self, source):
        self._source = source

    def load(self,**kwargs):
        result = { key : self._read_data(value) for key, value in kwargs.items() }
        return result

    def _read_data(self, name: str):
        with open(f'{self._source}/{name}.json') as json_data:
            data = json.load(json_data)
            return data
        