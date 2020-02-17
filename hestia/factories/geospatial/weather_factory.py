from hestia.models.geospatial.weather import Weather
from hestia.models.geospatial.weather_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory


class WeatherFactory(ModelFactory):
    '''Creates country instances from differrent data sources'''

    def __init__(self, eco_clim_zone_factory):
        super().__init__()

    def create(self, key):
        data = self._get_record(key)
        instance = Weather()

        return self._map(instance, data)

    def _get_record(self, key):
        df = self._data_frame
        if df is None:
            df = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        pass

    def _map(self, instance, data_row):
        return super()._map(instance, data_row, MODEL_MAPPING['column_names'].values())