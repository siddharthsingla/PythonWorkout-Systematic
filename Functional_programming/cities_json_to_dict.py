import json
def cities_json_to_dict():
    with open("cities.json") as fin:
        cities = json.load(fin)
    return {city['city']: city['population'] for city in cities}

print(cities_json_to_dict())
print(len(cities_json_to_dict()))