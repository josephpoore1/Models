from hestia.models.farmed_crop import FarmedCrop
from hestia.models.references.repository import ReferencesRepository

import numpy as np


class FertilizerPesticideAndOtherInputsEmissions:
    co2: float
    so2: float
    po4: float

    def __init__(self, references_repository: ReferencesRepository):
        self._repository = references_repository

    def calculate_for(self, crop: FarmedCrop):
        self._calculate_po4(crop)
        self._calculate_co2(crop)
        self._calculate_so2(crop)

    def _calculate_po4(self,crop: FarmedCrop):
        fertilizer_avg_eutr = self._repository.get_average_eutrophication_inputs()
        synth_n_inputs = self._repository.get_synth_n_emissions()
        infrastructure_emissions = self._repository.get_emissions_from_machinery_and_infrastructure()
        matmul_synth_fertilizers = np.matmul(crop.activities.fertilizing.synthetic.composition.series(), synth_n_inputs['eutr'])

        self.po4 = sum((
            crop.activities.fertilizing.synthetic.n * (fertilizer_avg_eutr['synthetic_fertilizer'] if np.isnan(matmul_synth_fertilizers) else matmul_synth_fertilizers),
            crop.activities.fertilizing.synthetic.p * fertilizer_avg_eutr['synthetic_phosprorus'],
            crop.activities.fertilizing.synthetic.k * fertilizer_avg_eutr['potassium'],
            sum((crop.activities.fertilizing.lime, crop.activities.fertilizing.dolomite)) * fertilizer_avg_eutr['lime'],
            (0 if np.isnan(crop.infrastructure.plastic) else crop.infrastructure.plastic) * infrastructure_emissions.loc['eutr','plastic'],
            (0 if np.isnan(crop.activities.pest_management.amount) else crop.activities.pest_management.amount) * fertilizer_avg_eutr['pesticide']
        ))

    def _calculate_so2(self,crop: FarmedCrop):
        fertilizer_avg_ghg = self._repository.get_average_acidification_inputs()
        synth_n_inputs = self._repository.get_synth_n_emissions()
        infrastructure_emissions = self._repository.get_emissions_from_machinery_and_infrastructure()
        matmul_synth_fertilizers = np.matmul(crop.activities.fertilizing.synthetic.composition.series(), synth_n_inputs['acid'])

        self.so2 = sum((
            crop.activities.fertilizing.synthetic.n * fertilizer_avg_ghg['synthetic_fertilizer'] if np.isnan(matmul_synth_fertilizers) else matmul_synth_fertilizers,
            crop.activities.fertilizing.synthetic.p * fertilizer_avg_ghg['synthetic_phosprorus'],
            crop.activities.fertilizing.synthetic.k * fertilizer_avg_ghg['potassium'],
            sum((crop.activities.fertilizing.lime, crop.activities.fertilizing.dolomite)) * fertilizer_avg_ghg['lime'],
            (0 if np.isnan(crop.infrastructure.plastic) else crop.infrastructure.plastic) * infrastructure_emissions.loc['acid','plastic'],
            (0 if np.isnan(crop.activities.pest_management.amount) else crop.activities.pest_management.amount) * fertilizer_avg_ghg['pesticide']
        ))

    def _calculate_co2(self,crop: FarmedCrop):
        fertilizer_avg_ghg = self._repository.get_average_ghg_inputs()
        synth_n_inputs = self._repository.get_synth_n_emissions()
        infrastructure_emissions = self._repository.get_emissions_from_machinery_and_infrastructure()
        matmul_synth_fertilizers = np.matmul(crop.activities.fertilizing.synthetic.composition.series(), synth_n_inputs['gwp'])

        self.co2 = sum((
            crop.activities.fertilizing.synthetic.n * fertilizer_avg_ghg['synthetic_fertilizer'] if np.isnan(matmul_synth_fertilizers) else matmul_synth_fertilizers,
            crop.activities.fertilizing.synthetic.p * fertilizer_avg_ghg['synthetic_phosprorus'],
            crop.activities.fertilizing.synthetic.k * fertilizer_avg_ghg['potassium'],
            sum((crop.activities.fertilizing.lime, crop.activities.fertilizing.dolomite)) * fertilizer_avg_ghg['lime'],
            (0 if np.isnan(crop.infrastructure.plastic) else crop.infrastructure.plastic) * infrastructure_emissions.loc['ghg','plastic'],
            (0 if np.isnan(crop.activities.pest_management.amount) else crop.activities.pest_management.amount) * fertilizer_avg_ghg['pesticide']
        ))
    