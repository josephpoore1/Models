from hestia.models.activities.fertilizers.synthetic.synthetic_fertilizer import SyntheticFertilizer
from hestia.models.activities.fertilizers.organic.organic_fertilizer import OrganicFertilizer
from hestia.models.activities.fertilizers.excreta.excreta import Excreta
import numpy as np

class Fertilizers:
    organic: OrganicFertilizer
    synthetic: SyntheticFertilizer
    excreta: Excreta
    lime: float
    dolomite: float

    def total_n(self):
        return np.sum(self.synthetic.n, self.organic.n, self.excreta.n)
