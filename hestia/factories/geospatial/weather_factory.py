from hestia.models.geospatial.weather import Weather
from hestia.models.geospatial.weather_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory

numeric_columns=['pet',
                 'winter_type_corr',
                 'avg_temp',
                 'precip',
                 'eco_clim_zone']


class WeatherFactory(ModelFactory):
    '''Creates country instances from differrent data sources'''

    def __init__(self, eco_clim_zone_factory):
        super().__init__()

    def create(self, key):
        data = self._get_record(key)
        instance = Weather()

        instance.precipitation = data['precip']
        instance.winter_type_corr=data['winter_type_corr']
        instance.pet=data['pet']
        instance.average_temperature=data['avg_temp']
        instance.eco_clim_zone=data['eco_clim_zone']

        return instance

    def _get_record(self, key):
        df = self._data_frame
        if df is None:
            df = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'],
                                        numeric_columns)
        return data_table.loc[key]

    def _gapfill(self, data_frame):
        pass