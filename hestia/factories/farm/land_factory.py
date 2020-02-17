from hestia.models.farm.land import Land
from hestia.models.farm.land_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory


class LandFactory(ModelFactory):
    def __init__(self, soil_factory, weather_factory, location_factory):
        super().__init__(self)
        self._soil_factory = soil_factory
        self._weather_factory = weather_factory
        self._location_factory = location_factory

    def create(self, land_key):
        '''Implements the creation logic for land, add related business rules here '''
        data = self._get_record(land_key)
        instance = Land()

        self._set_location(instance, land_key)
        self._set_weather(instance, land_key)
        self._set_soil(instance, land_key)

        return self._map(instance, data)

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        pass

    def _map(self, instance: Land, data: dict):
        instance.area = data['aera']
        instance.sp = data['sp']
        instance.geography = data['geography_spec']
        return instance

    def _set_location(self, instance: Land, location_key):
        location = self._location_factory.create(location_key)
        instance.location = location

    def _set_soil(self, instance: Land, soil_key):
        soil = self._soil_factory.create(soil_key)
        instance.soil = soil

    def _set_weather(self, instance: Land, weather_key):
        weather = self._weather_factory.create(weather_key)
        instance.weather = weather
