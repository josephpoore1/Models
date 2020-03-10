from hestia.factories.model_factory import ModelFactory
from hestia.models.coefficients.residue.residue_est_from_dm_yield_mapping import MODEL_MAPPING


class ResidueEstimationFromDMYield(ModelFactory):
    crop_name: float
    slope: float
    intercept: float
    n_content_ag: float
    n_content_bg: float
    combustion: float
    ratio_ag_to_bg: float

    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        instance = ResidueEstimationFromDMYield()
        df = self._get_data_frame(MODEL_MAPPING)
        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._map(instance, data_table.loc[key], MODEL_MAPPING['column_names'].values())

    def _gapfill(self, data_frame):
        pass

    def create(self, key):
        pass