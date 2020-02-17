from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.residue_management import ResidueManagement, CropResidue
from hestia.models.crops.residue.residue_mapping import MODEL_MAPPING
from hestia.models.measures.energy import Energy


class ResidueManagementFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data = self._data_frame
        if data is None:
            data = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        # use data_table to get gapfills
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        pass

    def create(self, key):
        record = self._get_record(key)

        residue_mgmt = ResidueManagement()
        self._set_crop_residue(residue_mgmt, record)

        return residue_mgmt

    def _set_crop_residue(self, instance, record):
        crop_residue = CropResidue()
        crop_residue.above_ground_remaining = record['ag_remaining']
        crop_residue.below_ground_remaining = record['bg_remaining']
        crop_residue.burnt_kg = record['burnt_kg']
        crop_residue.burnt_percent = record['burnt_prct']
        crop_residue.removed = record['removed']
        crop_residue.total = record['total']
        instance.residue = crop_residue
