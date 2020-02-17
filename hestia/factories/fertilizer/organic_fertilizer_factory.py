from hestia.factories.model_factory import ModelFactory

class OrganicFertilizerFactory(ModelFactory):
    def _get_record(self, key):
        pass

    def _gapfill(self, data_fame):
        pass

    def create(self, key):
        data = self._get_record(key)

    def __init__(self):
        super().__init__()
