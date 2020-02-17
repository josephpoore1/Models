from hestia.models.farm.machinery.machinery import Machinery
from hestia.models.activities.irrigation.irrigation import Irrigation
from hestia.models.activities.processing.crop_processing import ProcessingInfrastructure
from hestia.models.farm.plant_infrastructure import PlantInfrastructure


class FarmInfrastructure:
    machinery: Machinery
    irrigation: Irrigation
    processing: ProcessingInfrastructure
    plant: PlantInfrastructure
    plastic: float
