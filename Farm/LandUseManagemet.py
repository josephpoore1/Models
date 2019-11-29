from dataclasses import dataclass
from datetime import timedelta

@dataclass
class LandUseManagement:
    cultivation_duration: timedelta
    crop_allocation: float
    fallow_allocation: float
    