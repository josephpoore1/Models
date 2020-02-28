from hestia.models.object_model import ObjectModel
from hestia.models.farm.machinery.machinery import Machinery
from hestia.models.farm.plant_infrastructure import PlantInfrastructure


class FarmInfrastructure(ObjectModel):
    machinery: Machinery
    plant: PlantInfrastructure
    plastic: float

    def __init__(self):
        super().__init__()
