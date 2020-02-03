from dataclasses import dataclass
from country import Country

@dataclass
class Land:
    country: Country
    total_area: float


