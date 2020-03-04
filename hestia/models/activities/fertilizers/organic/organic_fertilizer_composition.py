class OrganicFertilizerComposition:
    liquid_or_slurry: float
    solid: float
    compost: float
    green_manure: float

    def to_series(self):
        return (self.liquid_or_slurry, self.solid, self.compost, self.green_manure)
