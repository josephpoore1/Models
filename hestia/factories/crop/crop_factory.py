from hestia.factories.model_factory import ModelFactory
from hestia.models.crops.crop import Crop


class CropFactory(ModelFactory):
    def _get_record(self, key):
        pass

    def _gapfill(self, data_frame):
        pass

    def __init__(self, crop_characteristics_factory, crop_composition_factory, crop_prouctivity_factory):
        super().__init__()
        self._crop_characteristics_factory = crop_characteristics_factory
        self._crop_composition_factory = crop_composition_factory
        self._crop_productivity_factory = crop_prouctivity_factory

    def create(self, key):
        crop = Crop()
        crop.characteristics= self._crop_characteristics_factory.create(key)
        crop.composition= self._crop_composition_factory.create(key)
        return crop