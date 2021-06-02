import json

def read_json(data):
    with open(data, "r", encoding='utf-8') as file:
        result = json.load(file)
    return result

print(read_json)