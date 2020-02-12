from abc import ABC, abstractmethod
from hestia.models.farm.land import Land
from hestia.models.geospatial.position import  Position
from hestia.factories.model_factory import ModelFactory

MODEL_MAPPING=dict(
    location=r'C:\observations\database.csv',
    separator='|',
    id_key='id',
    coulmn_names={
        'id': 'AQ',
        'crop_name': 'MI',
        'slope': 'PC',
        'slope_len': 'PB',
        'country': 'I'
    }
)


class BaseFactory(ABC):
    @abstractmethod
    def _map(self):

class LandFactory(ModelFactory, BaseFactory):
    def __init__(self):
        pass

    def create(self, land_key):
        data = self._get_data(land_key)
        instance = Land()
        if data is None:
            return instance

        instance.soil = self._soil_factory.create(soil_key)

        return self._map(instance, data)

    def _map(self, instance: Land, data: dict):
        instance.slope = data['slope']
        instance.slope_len = data['slope_len']
        instance.country = data['country']
        instance.sp=data['sp']
        instance.geography=data['geography_spec']
        instance.coord = Position(data['lat'], data['lon'])

        return instance

    def _get_data(self, key):
        data = self._data_frame
        if data is None:
            data = self._get_observations_data(MODEL_MAPPING['location'], MODEL_MAPPING['coulmn_names'])

        return data[key]