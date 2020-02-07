from hestia.factories.observations_factory import ObservationsFactory
from hestia.models.crops.crop_productivity import CropProductivity

DATA_MAPPING = dict(
    location=r'standardisation',
    id_key='id',
    column_names= {
        'nursery_duration': 'Table_OrchardCrops_NursDur',
        'sapling_yield': 'Table_OrchardCrops_SapYield',
        'orch_density': 'Table_OrchardCrops_OrchDens',
        'cultiv_duration': 'Table_OrchardCrops_CultDur',
        'fallow_period': 'Table_OrchardCrops_FallowDur',
        'non_bear_duration': 'Table_OrchardCrops_NonBearDur'
    }
)


class CropProductivityFactory(ObservationsFactory):
    def create(self, key):
        instance=CropProductivity()
        data_row=self._get_record(key)

    def _map(self, data_row, instance: CropProductivity):
        instance.cultiv_duration=data_row['cultiv_duration']
        instance.fallow_period=data_row['fallow_period']
        instance.non_bear_duration=data_row['non_bear_duration']
        instance.nursery_duration=data_row['nursery_duration']
        instance.orch_density=data_row['orch_density']
        instance.sapling_yield=data_row['sapling_yield']

    def _get_record(self, key):
        data=self._get_data_frame()
