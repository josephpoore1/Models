from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.fertilizers.synthetic.synthetic_fertilizer import SyntheticFertilizer
from hestia.models.activities.fertilizers.synthetic.synthetic_fertilizer_composition import SyntheticFertilizerComposition
from hestia.models.activities.fertilizers.synthetic.synthetic_fertilizer_mapping import MODEL_MAPPING


class SyntheticFertilizerFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        pass

    def create(self, key):
        record = self._get_record(key)

        instance = SyntheticFertilizer()
        self._set_composition(instance, record)
        self._map(instance, record)

        return instance

    def _map(self, instance, data):
        instance.n_amount = data['n_amount']
        instance.p_amount = data['p_amount']
        instance.k_amount = data['k_amount']

    def _set_composition(self, instance, record):
        composition = SyntheticFertilizerComposition()
        composition.AN_ACl_NP_KN_NPK = record['an_acl_np_kn_npk']
        composition.AnhA_AquaA = record['anha_aquaa']
        composition.AP_DAP_MAP = record['ap_dap_map']
        composition.AS = record['as']
        composition.CAN = record['can']
        composition.UAN_SOLU = record['uan_solu']
        composition.UREA_UAS = record['urea_uas']
        instance.composition = composition
