from hestia.factories.crop.farmed_crop_factory import FarmedCropFactory
from hestia.factories.crop.crop_factory import CropFactory
from hestia.factories.crop.crop_composition_factory import CropCompositionFactory
from hestia.factories.crop.crop_productivity_factory import CropProductivityFactory
from hestia.factories.crop.crop_characterstics_factory import CropCharacteristicsFactory
from hestia.factories.activities.crop_activities_factory import CropActivitiesFactory
from hestia.factories.farm.field_factory import FieldFactory
from hestia.factories.farm.farm_infrastructure_factory import FarmInfrastructureFactory
from hestia.factories.activities.fertilizing_factory import FertilizingFactory
from hestia.factories.activities.pests_management_factory import PestsManagementFactory
from hestia.factories.activities.residue_management_factory import ResidueManagementFactory
from hestia.factories.activities.land_management_factory import LandManagementFactory
from hestia.factories.activities.crop_processing_factory import CropProcessingFactory
from hestia.factories.activities.irrigation_factory import IrrigationFactory


class FarmedCropBuilder:
    def __init__(self):
        _crop_characteristics_factory = CropCharacteristicsFactory()
        _crop_composition_factory = CropCompositionFactory()
        _crop_prouctivity_factory = CropProductivityFactory()
        _crop_factory = CropFactory(_crop_characteristics_factory, _crop_composition_factory, _crop_prouctivity_factory)

        _fertilizing_factory = FertilizingFactory(_of_factory, sf_factory, excreta_factory)
        _pests_mgmt_factory = PestsManagementFactory()
        _residue_mgmt_factory = ResidueManagementFactory()
        _land_mgmt_factory = LandManagementFactory()
        _crop_processing_factory = CropProcessingFactory()
        _irrigation_factory = IrrigationFactory()

        _crop_activities_factory = CropActivitiesFactory( _fertilizing_factory, _pests_mgmt_factory, _residue_mgmt_factory,
                                                          _land_mgmt_factory, _crop_processing_factory, _irrigation_factory)
        _land_factory =
        _field_factory = FieldFactory(_land_factory)

        _machinery_factory =
        _processing_factory =
        _plant_factory =

        _infrastructure_factory = FarmInfrastructureFactory(_machinery_factory, _processing_factory, _plant_factory)

        main_factory = FarmedCropFactory(_crop_factory, _crop_activities_factory,
                                         _field_factory, _infrastructure_factory)

    def build_crop(self, key):

        farmed_crop = self.main_factory.create()