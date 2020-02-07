from hestia.models.crops.crop import Crop

DATA_MAPPING = dict(
    location=r'observations.csv',
    separator='|',
    id_key='id',
    column_names= {
        'id': 'AQ',
        'amount': 'NN',
        'hours': 'NO',
        'plastic': 'NP',
        'energy_disel': 'NM'
    }
)

class CropFactory:
    def __init__(self, crop_characteristics_factory, crop_composition_factory, crop_prouctivity_factory):
        self._crop_characteristics_factory=crop_characteristics_factory
        self._crop_composition_factory=crop_composition_factory
        self._crop_productivity_factory=crop_prouctivity_factory

    def create(self, key):
        new_crop= Crop()

        new_crop.characteristics=self._crop_characterstics_factory.create(key)
        new_crop.composition=self._crop_composition_factory(key)
        new_crop.productivity=self._crop_productivity_factory(key)

        return  new_crop