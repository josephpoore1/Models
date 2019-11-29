from dataclasses import dataclass
from Geospatial import Country

@dataclass
class Farm:
    id: int 
    name: str
    fields: list
    infrastructure: list
    machinery: list
    county: Country