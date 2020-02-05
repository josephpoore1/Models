from ...models.farmed_crop import FarmedCrop
from ...data_client.data_client import DataClient
class FarmedCropFactory:

    def __init__(self, data_client):
        self._data_client = data_client
        self._data_client = DataClient()

    def _get_data(self, crop_key):
        crop_data = self._data_client.load(crop_key)

    def create(self, crop_key):
        data = _get_data(crop_key)

    def create_from_key(self, key, value):
