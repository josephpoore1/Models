from file_loaders.json_loader import JsonLoader

class DataClient:
    def __init__(self, data_loader: JsonLoader):
        self._data_loader= data_loader
    
    def load_from_directory(self, **names):
        data = self._data_loader.load(names)
        

    def load_from_service(self):
        pass
    
