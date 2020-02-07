from dataclasses import dataclass

@dataclass
class Energy:
    amount: float
    sourceType: str
    

@dataclass
class Disel(Energy):
    sourceType: "Disel"

    def __init__(self, amount):
        self.amount=amount

@dataclass
class Electricity(Energy):
    sourceType: "Electricity"

    def __init__(self, amount):
        self.amount=amount

