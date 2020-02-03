from dataclasses import dataclass
from ..geospatial.country import Country

@dataclass
class Farm:
    id: int 
    name: str
    fields: list
    infrastructure: list
    machinery: list
    county: Country