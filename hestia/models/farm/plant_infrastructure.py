from hestia.models.object_model import ObjectModel


class PlantInfrastructure(ObjectModel):
    type: str
    glass: float
    plastic: float
    rockwool: float
    steel: float
    aluminium: float
    iron: float
    concrete: float
    wood: float

    def __init__(self):
        super().__init__()
