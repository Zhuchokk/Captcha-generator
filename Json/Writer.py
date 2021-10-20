import json


class Writer:
    def __init__(self):
        pass

    def write_filename(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)
