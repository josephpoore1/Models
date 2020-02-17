from hestia.factories.model_factory import ModelFactory
from hestia.models.activities.processing.crop_processing import CropProcessing
from hestia.models.activities.processing.crop_processing_mapping import MODEL_MAPPING
from hestia.models.measures.energy import Energy

class CropProcessingFactory(ModelFactory):
     def __init__(self):
         super().__init__()

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
         processing_energy = Energy(record['drying_electr'], record['drying_fuel'])
         processing = CropProcessing(processing_energy)

         return processing
