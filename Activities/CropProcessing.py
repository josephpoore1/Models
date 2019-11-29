from dataclasses import dataclass
from ValueObjects import Energy

@dataclass
class CropProcessing:
    total_energy_use: Energy