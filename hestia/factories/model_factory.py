"""
Responsible for instantiating reference data models 
from diferrent data sources

Use data_client to supply data loading mechanism
"""
from lookups.residue_estimation_from_area import ResidueEstimationFromArea
from lookups.residue_estimation_from_dm_yield import ResidueEstimationFromDMYield

class ResidueEstimationFromAreaFactory:
    _mapping: dict

    def __init__(self, data_client, mapping):
        self._data_client = data_client
        self._mapping = mapping
    
    def create_residue_estimation_from_area(self, crop_name: str):
        data = self._data_client.load()

        instance = ResidueEstimationFromArea()
        instance.ag_dm_yrs = data['ag_dm_yrs']