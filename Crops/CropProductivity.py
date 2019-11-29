from dataclasses import dataclass
from datetime import timedelta

@dataclass
class CropProductivity:
    nursery_duration: float
    sapling_yield: float
    cultiv_duration: float
    orch_density: float
    fallow_period : float
    non_bear_duration: float