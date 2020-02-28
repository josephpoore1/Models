from hestia.models.object_model import ObjectModel


class Soil(ObjectModel):
    def __init__(self):
        super().__init__()

    phH20: float
    clay: float
    sand: float
    nitrogen: float
    phosphorus: float
    org_carbon: float
    drainage_class: float
    loss_to_auqatics: float
    erodibility: float

