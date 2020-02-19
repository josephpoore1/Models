from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.fertilizers.fertilizers import Fertilizers
from hestia.models.activities.fertilizers.fertilizers_mapping import MODEL_MAPPING


class FertilizingFactory(ModelFactory):
     def __init__(self, organic_fertilizer_factory, synthetic_fertilizer_factory, excreta_factory):
         super().__init__()
         self._organic_fertilizer_factory = organic_fertilizer_factory
         self._synthetic_fertilizer_factory = synthetic_fertilizer_factory
         self._excreta_factory = excreta_factory

     def _get_record(self, key):
         data = self._data_frame
         if data is None:
             data = self._get_data_frame(MODEL_MAPPING)

         data_table = self._create_table(data, MODEL_MAPPING['column_names'],
                                         MODEL_MAPPING['id_key'])
         # use data_table to get gapfills
         return data_table.loc[key]

     def _gapfill(self, data_fame):
         pass

     def create(self, key):
         record = self._get_record(key)
         fertilizers = Fertilizers()

         self._map(fertilizers, record)
         self._set_organic_fertilizer(fertilizers, key)
         self._set_synthetic_fertilizer(fertilizers, key)
         self._set_excreta(fertilizers, key)

         return fertilizers

     def _map(self, instance, data):
         instance.dolomite = data['dolomite']
         instance.lime = data['lime']

     def _set_synthetic_fertilizer(self, instance, key):
         instance.synthetic = self._synthetic_fertilizer_factory.create(key)

     def _set_organic_fertilizer(self, instance, key):
         instance.organic = self._organic_fertilizer_factory.create(key)

     def _set_excreta(self, instance, key):
         instance.excreta = self._excreta_factory.create(key)