from hestia.models.activities.fertilizers.synthetic.synthetic_fertilizer import SyntheticFertilizer
from hestia.models.activities.fertilizers.organic.organic_fertilizer import OrganicFertilizer
from hestia.models.activities.fertilizers.excreta.excreta import Excreta


class Fertilizers:
    organic: OrganicFertilizer
    synthetic: SyntheticFertilizer
    excreta: Excreta
    lime: float
    dolomite: float

    def total_n(self):
        return sum((self.synthetic.n, self.organic.n, self.excreta.n))
