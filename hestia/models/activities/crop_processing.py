from dataclasses import dataclass
from ..measures.energy import Energy

@dataclass
class CropProcessing:
    total_energy_use: Energy