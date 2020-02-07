from hestia.models.geospatial.country import Country


class CountryFactory:
    def __init__(self, data_client):
        self._data_client = data_client

    def create(self, key, data_frame):
        instance = Country()

        instance.name = data_frame[key].name