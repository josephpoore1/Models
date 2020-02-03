"""
Responsible for instantiating reference data models 
from diferrent data sources

Use data_client to supply data loading mechanism
"""
from lookups.residue_estimation_from_area import ResidueEstimationFromArea
from lookups.residue_estimation_from_dm_yield import ResidueEstimationFromDMYield
from ..data_client.data_client import DataClient

import pandas as pd

class ResidueEstimationFromAreaFactory:
    _mapping: dict
    _data_client: DataClient

    def __init__(self, mapping, data_client):
        self._data_client = data_client
        self._mapping = mapping
    
    def create(self, crop_name: str):
        pdFrame= self._get_data_frame().set_index(crop_name)

        result= ResidueEstimationFromArea(crop_name)
        (result.ag_dm_yrs, result.bg_dm_yrs, result.n_content_ag, result.n_content_bg, result.combustion_factor) = pdFrame.loc[crop_name]
        return result

    def _get_data_frame(self):
        dataResult= self._data_client.load_from_files(**self._mapping)
        pdFrame= pd.DataFrame(data= dataResult.Values(), columns= dataResult.Keys())
        return pdFrame.transpose()

class ResidueEstimationDMYieldFactory:
    _mapping: dict
    _data_client: DataClient

    def __init__(self, mapping, data_client):
        self._data_client = data_client
        self._mapping = mapping
    
    def create(self, crop_name: str):
        data = self._data_client.load_from_files()