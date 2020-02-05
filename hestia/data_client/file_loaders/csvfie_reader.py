import pands as pd


class CSVFileReader:
    def __init__(self, source):
        self._source = source

    def read_data(self, file_name, delimiter, **kwargs):
        data = pd.read_csv(f'{self._source}/{file_name}', delimiter= delimiter, 
                            nrows= kwargs['take_rows'], cols= kwargs['take_cols'])
        return data


