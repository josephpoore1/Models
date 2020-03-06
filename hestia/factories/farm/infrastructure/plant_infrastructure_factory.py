from hestia.models.farm.plant_infrastructure import PlantInfrastructure
from hestia.models.farm.plant_infrastructure_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory

import numpy as np

class PlantInfrastructureFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def create(self, key):
        data = self._get_record(key)
        instance = PlantInfrastructure()
        return self._map(instance, data)

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._gapfill(data_table)
        return data_table.loc[key]

    def _map(self, instance: PlantInfrastructure, data):
        instance.type = data['type']
        instance.plastic = data['plastic']
        instance.aluminium = data['aluminium']
        instance.concrete = data['concrete']
        instance.glass = data['glass']
        instance.rockwool = data['rockwool']
        instance.iron = data['iron']
        instance.steel = data['steel']
        instance.wood = data['wood']

    def _gapfill(self, data_fame):
        data_fame.replace('-', np.NAN, inplace=True)
