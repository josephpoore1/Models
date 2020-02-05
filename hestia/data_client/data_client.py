from file_loaders.json_loader import JsonLoader
from file_loaders.csvfie_reader import CSVFileReader

import pandas as pd

class DataClient:
    def __init__(self, data_mapping, data_loader, ):
        self._data_loader= data_loader
        self._data_mapping= data_mapping


    def load(self, *crop_key, **names):
        """
        Loads data from an external source

        Parameters
        ----------
        crop_key: str or int, required
            A key of a crop for which the data 
            needs to be loaded:
            ex.: crop_name or crop
        """
        data = self._data_loader.load(**names)

    def _get_data_frame(self):
        dataResult= self._data_loader.load(**self._data_mapping)
        pdFrame= pd.DataFrame(data= dataResult.Values(), columns= dataResult.Keys())
        return pdFrame.transpose()
    
    def _get_data_series(self, crop_key):
        dataResult= self._data_loader.load(**self._data_mapping)
        frame = pd.DataFrame(dataResult)

