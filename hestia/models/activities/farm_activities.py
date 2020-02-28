from hestia.models.activities.fertilizers.fertilizers import Fertilizers
from hestia.models.activities.pesticides.pesticide_management import PesticideManagement
from hestia.models.activities.irrigation.irrigation import Irrigation
from hestia.models.activities.residue_management import ResidueManagement
from hestia.models.farm.land_management import LandManagement
from hestia.models.activities.tillage_management import TillageManagement
from hestia.models.activities.processing.crop_processing import CropProcessing


class FarmActivities:
    fertilizing: Fertilizers
    irrigation: Irrigation
    pest_management: PesticideManagement
    residue_management: ResidueManagement
    land_management: LandManagement
    crop_processing: CropProcessing
