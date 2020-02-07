import pandas as pd


class CSVReader:
    def __init__(self, location, delimiter):
        self._location = location
        self._delimiter = delimiter


    def read_rows(self, file_name, nrows, cols):
        return self._read_data(file_name, take_rows= nrows, take_cols= cols)

    def read_all(self, file_name):
        return self._read_data(file_name)

    def _read_data(self, file_name, **kwargs):
        data = pd.read_csv(f'{self._location}/{file_name}', delimiter= self._delimiter, 
                            nrows= kwargs['take_rows'], usecols= kwargs['take_cols'])
        return data


