from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.farm_activities import FarmActivities
from hestia.models.activities.farm_activities_mapping import MODEL_MAPPING

import numpy as np


class CropActivitiesFactory(ModelFactory):
    def __init__(self, fertilizing_factory, pests_mgmt_factory,
                 residue_mgmt_factory, land_mgmt_factory,
                 crop_processing_factory, irrigation_factory):
        super().__init__()
        self._fertilizing_factory = fertilizing_factory
        self._pests_mgmt_factory = pests_mgmt_factory
        self._residue_mgmt_factory = residue_mgmt_factory
        self._land_mgmt_factory = land_mgmt_factory
        self._crop_processing_factory = crop_processing_factory
        self._irrigation_factory = irrigation_factory

    def _get_record(self, key):
        data = self._data_frame
        if data is None:
            data = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        self._gapfill(data_table)
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        '''Implement this ig you need to gapfill missing data'''
        data_fame.replace('-', np.NAN, inplace=True)

    def create(self, key):
        activities_data = self._get_record(key)

        # fetch data from source and use mapping key values
        # to get composition parts
        # e.g.: irrigation = activities_data['irrigation_key']

        instance = FarmActivities()

        self._set_fertilizing(instance, key)
        self._set_irrigation(instance, key)
        self._set_pest_management(instance, key)
        self._set_residue_management(instance, key)
        self._set_land_management(instance, key)
        self._set_crop_processing(instance, key)

        return instance

    def _set_fertilizing(self, instance, key):
        instance.fertilizing = self._fertilizing_factory.create(key)

    def _set_irrigation(self, instance, key):
        instance.fertilizing = self._irrigation_factory.create(key)

    def _set_pest_management(self, instance, key):
        instance.pest_management = self._pests_mgmt_factory.create(key)

    def _set_residue_management(self, instance, key):
        instance.residue_management = self._residue_mgmt_factory.create(key)

    def _set_land_management(self, instance, key):
        instance.land_management = self._land_mgmt_factory.create(key)

    def _set_crop_processing(self, instance, key):
        instance.crop_processing = self._crop_processing_factory.create(key)
