'''
Note: Roots assumed to be removed in permanent 
crops at orchard end of life (except oil palm), consistent with best practice pest control
'''
from hestia.models.object_model import ObjectModel


class ResidueEstimationFromArea(ObjectModel):
    crop_name: str
    whole_plnt_ag_dm: int
    whole_plnt_bg_dm: int
    replanting_yrs: int
    prunnings_dm_yrs: int
    ag_dm_yrs: int
    bg_dm_yrs: int
    ref_flow_ha: int
    n_content_whole: float
    n_content_prunings: float
    n_content_ag: float
    n_content_bg: float
    combustion_factor: float
    source: str

    def __init__(self):
        super().__init__()
