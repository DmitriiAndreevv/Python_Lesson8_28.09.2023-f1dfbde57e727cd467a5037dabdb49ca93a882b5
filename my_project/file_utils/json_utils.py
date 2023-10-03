import json

def load_json(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)

def save_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
