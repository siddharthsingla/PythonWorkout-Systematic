from collections import defaultdict
def get_rainfall_stats():
    rainfall = defaultdict(list)
    while True:

        city = input("Enter name of a city: ").strip()
        if not city:
            break
        rain = int(input("Enter rainfall in inches: ").strip())
        rainfall[city].append(rain)
    for city, data in rainfall.items():
        print(f"{city}: {sum(data)}, {sum(data)/len(data)}")

def get_rainfall_statsv2():
    rainfall = {}
    while True:

        city = input("Enter name of a city: ").strip()
        if not city:
            break
        rain = int(input("Enter rainfall in inches: ").strip())
        if city in rainfall:
            try:
                rainfall[city].append(rain)
            except:
                rainfall[city] = [rainfall[city], rain]
        else:
            rainfall[city] = rain
    for city, data in rainfall.items():
        print(f"{city}: {sum(data)}, {sum(data)/len(data)}")

def get_rainfall_statsv3():
    rainfall = {}
    while True:

        city = input("Enter name of a city: ").strip()
        if not city:
            break
        rain = int(input("Enter rainfall in inches: ").strip())
        if city not in rainfall:
            rainfall[city] = []
        rainfall[city].append(rain)
    for city, data in rainfall.items():
        print(f"{city}: {sum(data)}, {sum(data)/len(data)}")

#another version where rain stats are stored in a list only if there are more than 1 values

def get_rainfall_statsv4():
    rainfall = {}
    while True:

        city = input("Enter name of a city: ").strip()
        if not city:
            break
        rain = int(input("Enter rainfall in inches: ").strip())
        if city not in rainfall:
            rainfall[city] = rain
        else:
            rainfall[city] = [rainfall[city], rain]
    for city, data in rainfall.items():
        if type(data) == list:
            print(f"{city}: {sum(data)}, {sum(data) / len(data)}")
        else:
            print(f"{city}: {data}")
get_rainfall_statsv4()