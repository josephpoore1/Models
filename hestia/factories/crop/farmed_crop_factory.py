from ...models.farmed_crop import FarmedCrop
from ...data_client.data_client import DataClient
from ...model_mappings.crop_residue_mappings import *
from ...model_mappings.observations_mapping import * 

class FarmedCropFactory:

    def __init__(self):
        self._observartions_client = DataClient(OBSERVATIONS)

    def _get_data(self, crop_key):
        crop_data = self._data_client.load(crop_key)

    def create(self, crop_key):