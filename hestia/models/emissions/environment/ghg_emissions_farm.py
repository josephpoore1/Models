
class FarmGhgEmissions:
    from_synthetic_fertilizer_direct: float
    from_synthetic_fertilizer_indirect: float
    from_organic_fertilizer: float
    from_excreta: float
    from_residue: float
    from_residue_burn: float

    def __init__(self, crop):
        self._crop = crop