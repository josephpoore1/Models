from hestia.models.crops.crop_characteristics import CropCharacteristics
from hestia.models.crops.crop_characteristics_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory

class CropCharacteristicsFactory(ModelFactory):
    def __init__(self):
        super().__init__(self)

    def create(self,key):
        data_row = self._get_record(key)
        instance = CropCharacteristics()
        return self.map(instance,data_row)

    def map(self,instance, data_row):
        instance.crop_name=data_row['crop_name']
        instance.crop_root_depth=['root_depth']
        return instance

    def _get_record(self, key):
        data=self._get_data_frame()
        if data is None:
            data=self._get_lookup_data(MODEL_MAPPING['location'],MODEL_MAPPING['column_names'])
        return data