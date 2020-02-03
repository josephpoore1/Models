from data_client import json_loader

class DataClient:
    def __init__(self, data_loader):
        self._data_loader = data_loader