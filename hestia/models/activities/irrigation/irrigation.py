from hestia.models.measures.energy import Energy


class Irrigation:
    type: str
    applied_amount: float
    energy: Energy
