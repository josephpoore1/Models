from hestia.factories.model_factory import ModelFactory
from hestia.models.farmed_crop import FarmedCrop
from hestia.models.farmed_crop_mapping import MODEL_MAPPING
from hestia.models.measures.crop_yield import CropYield


class FarmedCropFactory(ModelFactory):
    def __init__(self, crop_factory, crop_activities_factory, field_factory, infrastructure_factory):
        super().__init__()
        self._crop_factory = crop_factory
        self._crop_activities_factory = crop_activities_factory
        self._field_factory = field_factory
        self._infrastructure_factory = infrastructure_factory

    def create(self, crop_key):
        data=self._get_record(crop_key)

        instance=FarmedCrop()

        self._set_crop(instance, crop_key)
        self._set_field(instance, crop_key)
        self._set_activities(instance, crop_key)
        self._set_infrastructure(instance, crop_key)
        self._map(instance, data)

        return instance

    def _gapfill(self, data_fame):
        pass

    def _get_record(self, crop_key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        return data_table.loc[crop_key]

    def _map(self,instance:FarmedCrop, data):
        instance.crop_yield=CropYield(data['yield_dm'], data['yield_mkt'])
        instance.seed=data['seed']

    def _set_crop(self, instance, key):
        instance.crop = self._crop_factory.create(key)

    def _set_field(self, instance, key):
        instance.field = self._field_factory.create(key)

    def _set_activities(self, instance, key):
        instance.activities = self._crop_activities_factory.create(key)

    def _set_infrastructure(self, instance, key):
        instance.infrastructure = self._infrastructure_factory.create(key)