from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.residue_management import ResidueManagement, CropResidue
from hestia.models.crops.residue.residue_mapping import MODEL_MAPPING

import numpy as np
import pandas as pd


class ResidueManagementFactory(ModelFactory):
    def __init__(self):
        super().__init__()

    def _get_record(self, key):
        data = self._data_frame
        if data is None:
            data = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        # use data_table to get gapfills
        self._gapfill(data_table)
        return data_table.loc[key]

    def _gapfill(self, data_fame):
        data_fame.replace('-', np.NAN, inplace=True)

    def create(self, key):
        record = self._get_record(key)

        residue_mgmt = ResidueManagement()
        self._set_crop_residue(residue_mgmt, record)

        return residue_mgmt

    def _set_crop_residue(self, instance: ResidueManagement, record):
        crop_residue = CropResidue()
        crop_residue.above_ground_remaining = self._get_ag_remaining(record)
        crop_residue.below_ground_remaining = self._get_bg_remaining(record)
        crop_residue.burnt_kg = self._get_burnt_dm(record)
        crop_residue.burnt_percent = self._get_burnt_share(record)
        crop_residue.removed = self._get_removed_share(record)
        crop_residue.total = self._get_residue_total(record)

        instance.residue = crop_residue
        instance.method = record['management_type']

    def _get_residue_total(self, record):
        residue_n = self._references.get_residue_est_from_dm_yield()
        if np.isnan(record['total']):
            return self._get_ag_remaining(record) * residue_n['ag'] + self._get_bg_remaining(record) * residue_n['bg']
        else:
            return record['total']

    def _get_ag_remaining(self, record):
        estimation_from_dm_yield = self._references.get_residue_est_from_dm_yield()

        if np.isnan(record['above_ground_remaining']):
            yield_dm = record['yield_dm'] if pd.notna(record['yield_dm']) else record['yield_mkt'] * 0.85
            removed_share = self._get_removed_share(record)
            burnt_share = self._get_burnt_share(record)
            slope = estimation_from_dm_yield.loc[record['crop_name'] ,'slope']
            intercept = estimation_from_dm_yield.loc[record['crop_name', 'intercept']]

            return (yield_dm * slope + intercept * 1000) * (1-removed_share) * (1-burnt_share)

        else:
            return record['above_ground_remaining']

    def _get_bg_remaining(self, record):
        estimation_from_dm_yield = self._references.get_residue_est_from_dm_yield()

        if  np.isnan(record['below_ground_remaining']):
            yield_dm = record['yield_dm'] if pd.notna(record['yield_dm']) else record['yield_mkt'] * 0.85

            slope = estimation_from_dm_yield.loc[record['crop_name'] ,'slope']
            intercept = estimation_from_dm_yield.loc[record['crop_name', 'intercept']]
            ratio = estimation_from_dm_yield.loc[record['crop_name', 'ratio']]

            return (yield_dm * slope + intercept * 1000) * ratio
        else:
            return record['below_ground_remaining']

    def _get_burnt_share(self, record):
        if pd.notna(record['burnt_percent']):
            return record['burnt_percent']

        default_residue_burn = self._references.get_residue_burn_share()
        estimation_from_dm_yield = self._references.get_residue_est_from_dm_yield()

        return default_residue_burn.loc[record['crop_name'], record['country']] \
               * estimation_from_dm_yield.loc[record['crop_name'], 'combustion']

    def _get_removed_share(self, record):
        if pd.notna(record['removed']):
            return record['removed']

        default_residue_removal = self._references.get_residue_removed_share()
        return default_residue_removal.loc[record['crop_name'], record['country']]

    def _get_burnt_dm(self, record):
        estimation_from_dm_yield = self._references.get_residue_est_from_dm_yield()

        if np.isnan(record['burnt_kg']):
            yield_dm = record['yield_dm'] if pd.notna(record['yield_dm']) else record['yield_mkt'] * 0.85
            removed_share = self._get_removed_share(record)
            burnt_share = self._get_burnt_share(record)
            slope = estimation_from_dm_yield.loc[record['crop_name'] ,'slope']
            intercept = estimation_from_dm_yield.loc[record['crop_name', 'intercept']]

            return (yield_dm * slope + intercept * 1000) * (1-removed_share) * burnt_share