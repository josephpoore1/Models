import sys

from hestia.data_client.data_client import DataClient
from hestia.data_client.file_loaders.json_loader import JsonLoader
from hestia.factiories.model_factory import ModelFactory

def main(**kwargs):
    json_loader = JsonLoader(kwargs['location'])
    client = DataClient(json_loader)
    factory = ModelFactory(client)



if __name__ == "__main__":
    main(location= sys.argv[1], entity = sys.argv[2])

