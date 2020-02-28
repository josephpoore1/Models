'''
Source: IPCC (2006) Vol. 4 Table 2.6 and 11.2, with adjustments
'''
from hestia.models.object_model import ObjectModel


class ResidueEstimateFromDMYield(ObjectModel):
    crop_name: str
    slope: float
    intercept: float
    n_content_ag: float
    ratio_abv_below_gr: float
    n_content_bg: float
    combustion_factor: float
    source: str

    def __init__(self):
        super.__init__()

