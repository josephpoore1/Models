from hestia.models.farm.farm_infrastructure import FarmInfrastructure
from hestia.models.farm.farm_infrastructure_mapping import MODEL_MAPPING
from hestia.factories.model_factory import ModelFactory


class FarmInfrastructureFactory(ModelFactory):
    def __init__(self, machinery_factory, processing_factory, plant_factory):
        super().__init__()
        self._machinery_factory = machinery_factory
        self._processing_factory = processing_factory
        self._plant_factory = plant_factory

    def create(self, key):
        data = self._get_record(key)
        instance = FarmInfrastructure()
        self._set_processing(instance, key)
        self._set_machinery(instance, key)
        self._set_plant_infrastructure(instance, key)

        return self._map(instance, data)

    def _get_record(self, key):
        data_frame = self._data_frame
        if data_frame is None:
            data_frame = self._get_data_frame(MODEL_MAPPING)

        data_table = self._create_table(data_frame, MODEL_MAPPING['column_names'],
                                        MODEL_MAPPING['id_key'])
        return data_table.loc[key]

    def _map(self, instance: FarmInfrastructure, data):
        instance.amount = data['amount']
        instance.hours = data['hours']
        instance.plastic = data['plastic']
        return instance

    def _gapfill(self, data_fame):
        pass

    def _set_plant_infrastructure(self, instance: FarmInfrastructure, plant_infst_key):
        plant_infrastructure = self._plant_factory.create(plant_infst_key)
        instance.plant = plant_infrastructure

    def _set_processing(self, instance: FarmInfrastructure, processing_key):
        processing = self._processing_factory.create(processing_key)
        instance.processing = processing

    def _set_machinery(self, instance: FarmInfrastructure, machinery_key):
        machinery = self._machinery_factory.create(machinery_key)
        instance.machinery = machinery
