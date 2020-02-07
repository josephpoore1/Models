from hestia.factories.observations_factory import ObservationsFactory
from hestia.models.farm.farm_infrastructure import MachineryAndInfrastructure
from hestia.models.measures.energy import Energy, Disel, Electricity

import pandas as pd

DATA_MAPPING = dict(
    location=r'observations.csv',
    separator='|',
    id_key='id',
    column_names= {
        'id': 'AQ',
        'amount': 'NN',
        'hours': 'NO',
        'plastic': 'NP',
        'energy_disel': 'NM'
    }
)


class FarmInfrastructureFactory(ObservationsFactory):
    def __init__(self):
        super(self)


    def create(self, key):
        new_infrastructure=MachineryAndInfrastructure()
        series= self._get_record(key)

        new_infrastructure.amount=series['amount']
        new_infrastructure.hours=series['hours']
        new_infrastructure.plastic=series['plastic']
        new_infrastructure.energy = Disel(series['energy_disel'])

        return new_infrastructure

    def _get_series(self):
        if self.data_frame is None:
            column_names = DATA_MAPPING['column_names'].values()
            self.data_frame = self._get_data(DATA_MAPPING['location'], DATA_MAPPING['separator'], column_names)

    def _get_record(self, key):
        data = self._get_series()
        column_keys = DATA_MAPPING['column_names'].keys()
        index = DATA_MAPPING['id']
        data = self._data_frame.columns = column_keys
        data.set_index(index)
        return data.loc[key]
