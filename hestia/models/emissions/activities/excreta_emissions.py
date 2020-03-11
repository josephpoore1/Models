from hestia.models.farmed_crop import FarmedCrop
from hestia.models.emissions.chemical.chemical_emissions import ChemicalEmissions
from hestia.models.references.repository import ReferencesRepository

import numpy as np


class ExcretaEmissions:
    direct: float
    indirect: float

    def __init__(self, references_repository: ReferencesRepository, chemical_emissions: ChemicalEmissions):
        self._emissions = chemical_emissions
        self._references = references_repository

    def calculate_for(self, crop: FarmedCrop):
        self._calculate_direct(crop)
        self._calculate_indirect(crop)

    def _calculate_indirect(self, crop: FarmedCrop):
        emission_factors = self._references.get_n2o_from_fertilizers_and_residue()
        atomic_weights = self._references.get_atomic_weight_conversions()
        loss_factors = self._references.get_n_loss_factors()

        if np.isnan(self._emissions.nh3.excreta) or np.isnan(self._emissions.nox.excreta):
            self.indirect = crop.activities.fertilizing.excreta.n * loss_factors['organic'] \
                            + emission_factors['no3n'] * self._emissions.no3.excreta / atomic_weights['no3n_no3']
        else:
            self.indirect = sum((self._emissions.nh3.excreta /atomic_weights['nh3n_nh3'],
                                 self._emissions.nox.excreta /atomic_weights['non_no'])) \
                            + emission_factors['no3n'] * self._emissions.no3.excreta / atomic_weights['no3n_no3']

    def _calculate_direct(self, crop: FarmedCrop):
        gwp = self._references.get_gwp()
        self.direct = self._emissions.no2.excreta * gwp['n2o']
