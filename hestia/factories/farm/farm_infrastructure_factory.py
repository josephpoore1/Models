from hestia.factories.model_factory import ModelFactory
from hestia.models.farm.farm_infrastructure import MachineryAndInfrastructure
from hestia.models.measures.energy import Energy, Disel, Electricity

import pandas as pd

MODEL_MAPPING = dict(
    location=r'D:\ProArch\hestia\data\database.csv',
    separator='|',
    id_key='id',
    column_names= {
        'AQ': 'id',
        'NN': 'amount',
        'NO': 'hours',
        'NP':'plastic',
        'NM':'energy_disel'
    }
)


class FarmInfrastructureFactory(ModelFactory):
    def __init__(self):
        super(ModelFactory, self).__init__()

    def create(self, key):
        new_infrastructure=MachineryAndInfrastructure()
        series= self._get_record(key)

        new_infrastructure.amount=series['amount']
        new_infrastructure.hours=series['hours']
        new_infrastructure.plastic=series['plastic']
        new_infrastructure.energy = Disel(series['energy_disel'])

        return new_infrastructure

    def _get_series(self, key):
        data_frame = self._data_frame
        if self.data_frame is None:
            self.data_frame = self._get_data(MODEL_MAPPING['location'], MODEL_MAPPING['separator'], MODEL_MAPPING['column_names'], MODEL_MAPPING['id_key'])
        return data_frame.loc[key]

    def _get_record(self, key):
        data = self._get_series()
        column_keys = MODEL_MAPPING['column_names'].keys()
        index = MODEL_MAPPING['id']
        data = self._data_frame.columns = column_keys
        data.set_index(index)
        return data.loc[key]
