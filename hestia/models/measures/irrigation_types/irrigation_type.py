class IrrigationType:

    def __init__(self, name, field_appl_eff, conv_eff):
        self._name = name
        if  field_appl_eff > 1 or field_appl_eff < 0:
            raise ValueError("Field Application Efficiency should be a value between 0 and 1")
        self._field_appl_efficency = field_appl_eff
        if conv_eff > 1 or field_appl_eff < 0:
            raise ValueError("Conveyance Efficiency should be a value between 0 and 1")
        self._conveyance_efficency = conv_eff

class SurfaceIrrigation(IrrigationType):

    def __init__(self):
        self._name = "Surface"
        self._field_appl_eff = 0.6
        self._conveyance_efficency = .75

class SprinklerIrrigation(IrrigationType):

    def __init__(self):
        self._name = "Sprinkler"
        self._field_appl_eff = 0.75
        self._conveyance_efficency = 1

class LocalizedIrrigation(IrrigationType):

    def __init__(self):
        self._name = "Localized"
        self._field_appl_eff = 0.9
        self._conveyance_efficency = 1