from ..farmed_crop import FarmedCrop

class FarmEmissions:
    co2: float
    so2: float
    po4: float
    water_scarcity: float
    freshwt_withd: float
    land_use: float
    
    def __init__(self, crop: FarmedCrop):
        self._crop = crop
        