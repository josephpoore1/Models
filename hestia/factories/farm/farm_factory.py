from hestia.data_client.data_client import DataClient
from hestia.models.farm.farm import Farm
from hestia.factories.gespatial.country_factory import CountryFactory

import  pandas as pd

FARM_MODEL_MAP=dict(
    location=r'C:\observations\database.csv',
    separator='|',
    id_key='id',
    coulmn_names={
        'id': 'AQ',
        'latitude': 'M',
        'longitude': 'N',
        'sp': 'O'
    }
)

class FarmFactory:
    def __init__(self, country_factory: CountryFactory):
        self._country_factory = country_factory

    def create(self, key):
        self._get_series()
        new_farm = Farm()
        series = self._get_record(key)
        self._map(data_row=series, instance=new_farm)
        new_farm.county = self._country_factory.create(key)

        return new_farm

    def _map(self, data_row, instance: Farm):
        instance.name, = data_row['name']

    def set_data_frame(self, data_frame):
        self._data_frame = data_frame

    def _get_series(self):
        if self._data_frame is None:
            column_names = FARM_MODEL_MAP['column_names'].values()
            self.data_frame = self._get_csv_data(FARM_MODEL_MAP['location'], FARM_MODEL_MAP['separator'], column_names)

    def _get_record(self, key):
        column_keys = FARM_MODEL_MAP['column_names'].keys()
        index = FARM_MODEL_MAP['id']
        data = self._data_frame.columns = column_keys
        data.set_index(index)
        return data.loc[key]


