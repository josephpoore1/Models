from hestia.factories.model_factory import ModelFactory
from hestia.models.coefficients.residue_burn.crop_residue_burn_ef_mapping import MODEL_MAPPING


class CropResidueBurnEmissionFactors(ModelFactory):
    def __init__(self):
        ch4: float
        n2o: float
        nh3: float
        nox: float

    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        pass

    def _gapfill(self, data_frame):
        pass

    def create(self, key):
        instance = CropResidueBurnEmissionFactors()
        df = self._get_data_frame(MODEL_MAPPING)
        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._map(instance, data_table.loc[key], MODEL_MAPPING['column_names'].values())
        return instance