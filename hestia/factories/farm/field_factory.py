from hestia.data_client.data_client import DataClient
from hestia.models.farm.field import Field
from hestia.factories.model_factory import ModelFactory
from hestia.factories.geospatial.country_factory import CountryFactory

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

class FieldFactory(ModelFactory):
    def __init__(self, land_factory: LandFactory):
        self._land_factory = land_factory

    def create(self, key):
        self._get_data(key)
        instance = Field()

        instance.land = self._land_factory.create(key)

        return instance

    def _map(self, data, instance: Field):
        instance.name = data['name']

        return instance

    def _get_data(self):
        if self._data_frame is None:
            column_names = FARM_MODEL_MAP['column_names'].values()
            self.data_frame = self._get_csv_data(FARM_MODEL_MAP['location'], FARM_MODEL_MAP['separator'], column_names)

    def _get_record(self, key):
        column_keys = FARM_MODEL_MAP['column_names'].keys()
        index = FARM_MODEL_MAP['id']
        data = self._data_frame.columns = column_keys
        data.set_index(index)
        return data.loc[key]


