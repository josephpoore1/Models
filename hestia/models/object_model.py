import json


class ObjectModel(json.JSONEncoder):
    def __init__(self):
        super().__init__()

    def default(self, o):
        return o.__dict__