from dataclasses import dataclass
from Geospatial import Country

@dataclass
class Land:
    country: Country
    total_area: float


