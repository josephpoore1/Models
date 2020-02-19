'''
Source: IPCC (2006) Vol. 4 Table 2.6 and 11.2, with adjustments
'''


class ResidueEstimateFromDMYield:
    crop_name: str
    slope: float
    intercept: float
    n_content_ag: float
    ratio_abv_below_gr: float
    n_content_bg: float
    combustion_factor: float
    source: str
