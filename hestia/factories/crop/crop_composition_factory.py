from hestia.factories.model_factory import ModelFactory
from hestia.models.crops.crop_composition import CropComposition

import numpy as np


class CropCompositionFactory(ModelFactory):
    def _get_record(self, key):
        pass

    def _gapfill(self, data_frame):
        pass

    def __init__(self):
        super().__init__()

    def create(self, key):
        instance = CropComposition()
        return instance

