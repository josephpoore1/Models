from dataclasses import dataclass

from hestia.models.farm.land import Land


@dataclass
class Field:
    land: Land
