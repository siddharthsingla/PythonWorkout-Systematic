def get_rainfall():
    rainfall = {}
    while True:

        city = input("Enter name of a city: ").strip()
        if not city:
            break
        rain = int(input("Enter rainfall in inches: ").strip())
        rainfall[city] = rainfall.get(city, 0) + rain
    print(rainfall)

get_rainfall()