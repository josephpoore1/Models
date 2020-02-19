from hestia.models.farm.machinery.machinery import Machinery
from hestia.models.farm.plant_infrastructure import PlantInfrastructure


class FarmInfrastructure:
    machinery: Machinery
    plant: PlantInfrastructure
    plastic: float
