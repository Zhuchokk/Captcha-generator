import json


class Reader:
    def __init__(self, path_to_json):
        self.path = path_to_json

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(fp=f)
        return data

    def read_filename(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(fp=f)
        return data
