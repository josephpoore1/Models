from hestia.factories.model_factory import ModelFactory
from . import crop_factory, crop_characterstics_factory, crop_productivity_factory, crop_composition_factory
from hestia.models.farmed_crop import FarmedCrop
from hestia.models.measures.crop_yield import CropYield

import sys

DATA_MAPPING = dict(
    location=r'observations.csv',
    separator='|',
    id_key='id',
    column_names= {
        'id': 'AQ',
        'name': 'MI',
        'yield_dm': 'OF',
        'yield_mkt': 'OH',
        'seed': 'MK'
    }
)


class FarmedCropFactory(ModelFactory):
    def __init__(self, crop_factory, crop_activities_factory, field_factory, infrastructure_factory, machinery_factory):
        self._crop_factory = crop_factory
        self._crop_activities_factory = crop_activities_factory
        self._field_factory = field_factory
        self._infrastructure_factory = infrastructure_factory
        self._machinery_factory = machinery_factory

    def create(self, crop_key):
        data=self._get_data(crop_key)
        instance=FarmedCrop()

        instance.crop=self._crop_factory.create(crop_key)
        instance.activities=self._crop_activities_factory.create(crop_key)
        instance.field=self._field_factory.create(crop_key)
        instance.infrastructure=self._infrastructure_factory.create(crop_key)
        instance.machinery=self._machinery_factory.create(crop_key)
        return self._map(instance, data)

    def _get_data(self, crop_key):
        crop_data = self._get_observations_data(DATA_MAPPING['location'], DATA_MAPPING['separator'], DATA_MAPPING['column_names'])
        data=crop_data[crop_key]

        return data

    def _map(self,instance:FarmedCrop, data):
        instance.crop_yield=CropYield(data['yield_dm'], data['yield_mkt'])
        instance.farming_time=data['farm_duration']
        instance.seed=data['seed']


def main(**kwargs):
    print('Building a crop')
    c_factory = CropFactory()
    c_activites_factory = CropActivitiesFactory()
    field_factory = FieldFactory()
    infrastructure_factory = FarmInfrastructureFactory()
    machinery_factory = MachineryFactory()
    fc_factory = FarmedCropFactory(c_factory,c_activites_factory,field_factory,infrastructure_factory,machinery_factory)
    crop = fc_factory.create(kwargs['crop_key'])
    print('Done')
    print(crop)


if __name__ == '__main__':
    crop_key=sys.argv[1]
    main(crop_key)
