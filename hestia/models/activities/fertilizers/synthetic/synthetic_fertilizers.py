from dataclasses import dataclass
from .synthetic_fertilizer import SyntheticFertilizer


@dataclass
class AmmoniumSulphate(SyntheticFertilizer):
    amount: float
    name = "Ammonium Sulphate"
    chemical_formula = '((NH4)2SO4)'
    

@dataclass
class AmmoniumNitrate(SyntheticFertilizer):
    amount: float
    name = "Ammonium Nitrate"
    chemical_formula = "N2H4O3"


@dataclass
class AmmoniumChloride(SyntheticFertilizer):
    amount: float
    name = "Ammonium Chloride"
    chemical_formula = "NH4Cl"


@dataclass
class AnhydrousAmmonium(SyntheticFertilizer):
    amount: float
    name = "Anhydrous Ammonium"
    chemical_formula = "NH3"


@dataclass
class CalciumNitrate(SyntheticFertilizer):
    amount: float
    name = "Calcium Nitrate"
    chemical_formula = "Ca(NO3)2"


@dataclass
class NitricAcid(SyntheticFertilizer):
    amount: float
    name = "Nitric Acid"
    chemical_formula = "HNO3"
    fertilizer_type = super().fertilizer_type


class Program():
    def work(self):
        fert = AmmoniumChloride(200)
