from hestia.factories.model_factory import ModelFactory
from hestia.models.geospatial.soil import Soil
from hestia.models.geospatial.soil_mapping import MODEL_MAPPING

import numpy as np


class SoilFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def create(self, key):
        data = self._get_record(key)
        instance = Soil()
        return self._map(instance, data)

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._gapfill(data_table)
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        data_fame.replace('-', np.NAN, inplace=True)

    def _map(self, instance: Soil, data: dict):
        '''TODO: do tuple unpacking?'''
        instance.clay = data['clay']
        instance.drainage_class = data['drainage']
        instance.erodibility = data['erodibility']
        instance.loss_to_auqatics = data['loss_to_aquatics']
        instance.nitrogen = data['nitrogen']
        instance.org_carbon = data['org_carbon']
        instance.phH20=data['phH2O']
        instance.phosphorus =data['phos']
        instance.sand=data['sand']
        return instance
