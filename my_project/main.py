from file_utils import load_json, save_json

data = {'name': 'John', 'age': 30}
save_json(data, 'data.json')

loaded_data = load_json('data.json')
print(loaded_data)
