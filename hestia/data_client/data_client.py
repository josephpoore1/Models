from hestia.data_client.file_readers.reader_factory import ReaderFactory

import pandas as pd

reader_factory = ReaderFactory()


class DataClient:
    def __init__(self, configuration):
        self._data_reader= reader_factory.create_reader(configuration.type, data_type= configuration.data_type)

    def get_data_frame(self):
        dataResult= self._data_reader.read_all(**self._data_mapping)
        pdFrame= pd.DataFrame(data=dataResult.Values(), columns=dataResult.Keys())
        return pdFrame.transpose()
    
    def get_data_series(self, key):
        dataResult= self._data_reader.load(**self._data_mapping)
        return pd.DataFrame(dataResult)

