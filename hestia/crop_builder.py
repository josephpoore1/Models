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
from hestia.factories.activities.fertilizers.organic_fertilizer_factory import OrganicFertilizerFactory
from hestia.factories.activities.fertilizers.synthetic_fertilizer_factory import SyntheticFertilizerFactory
from hestia.factories.activities.fertilizers.excreta_factory import ExcretaFactory
from hestia.factories.farm.land_factory import LandFactory
from hestia.factories.geospatial.soil_factory import SoilFactory
from hestia.factories.geospatial.position_factory import PositionFactory
from hestia.factories.geospatial.eco_climate_zone_factory import EcoClimateZoneFactory
from hestia.factories.geospatial.weather_factory import WeatherFactory
from hestia.factories.geospatial.location_factory import LocationFactory
from hestia.factories.geospatial.country_factory import CountryFactory
from hestia.factories.farm.infrastructure.machinery_factory import MachineryFactory
from hestia.factories.farm.infrastructure.plant_infrastructure_factory import PlantInfrastructureFactory

class FarmedCropBuilder:
    def __init__(self):
        _crop_characteristics_factory = CropCharacteristicsFactory()
        _crop_composition_factory = CropCompositionFactory()
        _crop_prouctivity_factory = CropProductivityFactory()
        _crop_factory = CropFactory(_crop_characteristics_factory, _crop_composition_factory, _crop_prouctivity_factory)

        _organic_fertilizer_factory = OrganicFertilizerFactory()
        _synthetic_fertilizer_factory = SyntheticFertilizerFactory()
        _excreta_factory = ExcretaFactory()

        _fertilizing_factory = FertilizingFactory(_organic_fertilizer_factory, _synthetic_fertilizer_factory, _excreta_factory)
        _pests_mgmt_factory = PestsManagementFactory()
        _residue_mgmt_factory = ResidueManagementFactory()
        _land_mgmt_factory = LandManagementFactory()
        _crop_processing_factory = CropProcessingFactory()
        _irrigation_factory = IrrigationFactory()

        _crop_activities_factory = CropActivitiesFactory( _fertilizing_factory, _pests_mgmt_factory, _residue_mgmt_factory,
                                                          _land_mgmt_factory, _crop_processing_factory, _irrigation_factory)

        _soil_factory = SoilFactory()
        _eco_clim_zone_factory = EcoClimateZoneFactory()
        _weather_factory = WeatherFactory(_eco_clim_zone_factory)
        _position_factory = PositionFactory()
        _location_factory = LocationFactory(_position_factory)

        _land_factory = LandFactory(_soil_factory, _weather_factory, _location_factory)
        _field_factory = FieldFactory(_land_factory)

        _machinery_factory = MachineryFactory()
        _plant_factory = PlantInfrastructureFactory()

        _infrastructure_factory = FarmInfrastructureFactory(_machinery_factory, _plant_factory)

        self._main_factory = FarmedCropFactory(_crop_factory, _crop_activities_factory,
                                         _field_factory, _infrastructure_factory)

    def build_crop(self, key):
        farmed_crop = self._main_factory.create(key)
        return farmed_crop