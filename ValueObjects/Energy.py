from dataclasses import dataclass

@dataclass
class Energy:
    amount: float
    sourceType: str
    

@dataclass
class Disel(Energy):
    sourceType: "Disel"

@dataclass
class Electricity(Energy):
    sourceType: "Electricity"
    
