from hestia.factories.model_factory import ModelFactory

from hestia.models.geospatial.soil import Soil

a = list(MODEL_MAPPING['column_names'].values())


class SoilFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def create(self, key):
        data = self._get_data(key)
        instance = Soil()

        return self._map(instance, data)

    def _get_data(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_observations_data(MODEL_MAPPING['location'], MODEL_MAPPING['separator'], MODEL_MAPPING['column_names'],MODEL_MAPPING['id_key'])
        return data_frame.loc[key]

    def _map(self, instance: Soil, data: dict, a):
        '''TODO: do tuple unpacking?'''
        # instance.clay = data['clay']
        # instance.drainage_class = data['drainage']
        # instance.erodibility = data['erodibility']
        # instance.loss_to_auqatics = data['loss_to_aquatics']
        # instance.nitrogen = data['nitrogen']
        # instance.org_carbon = data['org_carbon']
        # instance.phH20=data['phH2Oinst']
        # instance.phosphorus =data['phos']
        # instance.sand=data['sand']
        for item in a:
            instance.__setattr__(item, data[item])
        return instance
