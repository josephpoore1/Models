from hestia.factories.model_factory import ModelFactory
from hestia.models.crops.crop_composition import CropComposition
from hestia.models.crops.crop_composition_mapping import MODEL_MAPPING

class CropCompositionFactory(ModelFactory):
    def __init__(self):
        super().__init__(self)

    def create(self):
        instance = CropComposition()

