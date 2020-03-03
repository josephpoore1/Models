import pandas as pd


class ExcelFileReader:
    def __init__(self, file_name):
        self._file_name = file_name

    def read_all(self):
        return pd.read_excel(self._file_name)

    def read_sheet(self, sheet_name, usecols=[':'], skiprows= 0, nrows= 1000000):
        return pd.read_excel(self._file_name,
                             sheet_name= sheet_name,
                             usecols= usecols,
                             skiprows= skiprows,
                             nrows= nrows)

    def read_address(self, address: str):
        sheet_name, sheet_address = address.split('!')
        start, end = sheet_address.split(':')
        col_start, row_start = start.lstrip('$').split('$')
        col_end, row_end = end.lstrip('$').split('$')
        take = int(row_end) - int(row_start)
        skip = int(row_start)

        return self.read_sheet(sheet_name,
                               usecols= [f'{col_start}:{col_end}'],
                               skiprows=skip,
                               nrows=take)