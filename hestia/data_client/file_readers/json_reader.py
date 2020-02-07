import json

class JsonReader:

    def __init__(self, source):
        self._source = source

    def read(self,**kwargs):
        result = { key : self._open(value) for key, value in kwargs.items() }
        return result

    def _open(self, name: str):
        with open(f'{self._source}/{name}.json') as json_data:
            data = json.load(json_data)
            return data
        