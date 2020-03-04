import numpy as np


class SyntheticFertilizerComposition:
    UREA_UAS: float
    AS: float
    UAN_SOLU: float
    AN_ACl_NP_KN_NPK: float
    CAN: float
    AnhA_AquaA: float
    AP_DAP_MAP: float

    def __init__(self):
        pass

    def series(self):
        return (self.UREA_UAS,
                self.AS,
                self.UAN_SOLU,
                self.AN_ACl_NP_KN_NPK,
                self.CAN,
                self.AnhA_AquaA,
                self.AP_DAP_MAP)

    def sum(self):
        return np.sum(self.series())
