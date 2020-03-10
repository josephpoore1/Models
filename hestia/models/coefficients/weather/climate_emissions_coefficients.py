from hestia.factories.model_factory import ModelFactory
from hestia.models.coefficients.weather.climate_emissions_coefficients_mapping import MODEL_MAPPING


class ClimateEmissionCoefficients(ModelFactory):
    id: int
    n2o_n: float
    nox_n: float

    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        pass

    def _gapfill(self, data_frame):
        pass

    def create(self, key):
        instance = ClimateEmissionCoefficients()
        df = self._get_data_frame(MODEL_MAPPING)
        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._map(instance, data_table.loc[key], MODEL_MAPPING['column_names'].values())