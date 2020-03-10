from hestia.factories.model_factory import ModelFactory
from hestia.models.coefficients.soil.p_loss_factors_crop_mapping import MODEL_MAPPING


class PhosphorusLossFactorsCrop(ModelFactory):
    country: str
    c1: float
    c2: float

    def __init__(self):
        super().__init()

    def _get_record(self, key):
        pass

    def _gapfill(self, data_frame):
        pass

    def create(self, key):
        instance = PhosphorusLossFactorsCrop()
        df = self._get_data_frame(MODEL_MAPPING)
        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._map(instance, data_table.loc[key], MODEL_MAPPING['column_names'].values())
        return instance
