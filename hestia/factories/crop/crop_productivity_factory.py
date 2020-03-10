from hestia.factories.model_factory import ModelFactory
from hestia.models.crops.crop_productivity import CropProductivity
from hestia.models.crops.crop_productivity_mapping import MODEL_MAPPING

import numpy as np


class CropProductivityFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _gapfill(self, data_frame):
        pass

    def create(self, key):
        instance=CropProductivity()
        data_row=self._get_record(key)
        if data_row is None:
            return  instance

    def _map(self, data_row, instance: CropProductivity):
        instance.cultiv_duration=data_row['cultiv_duration']
        instance.fallow_period=data_row['fallow_period']
        instance.non_bear_duration=data_row['non_bear_duration']
        instance.nursery_duration=data_row['nursery_duration']
        instance.orch_density=data_row['orch_density']
        instance.sapling_yield=data_row['sapling_yield']

    def _get_record(self, key):
        df = self._data_frame
        if df is None:
            df = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(df, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        return data_table.loc[key]
