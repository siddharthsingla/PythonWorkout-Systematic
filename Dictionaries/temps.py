from datetime import datetime, timedelta

temps = {'2022-12-22': 100, '2022-12-23': 200, '2022-12-21': 10}
def get_temps():
    tempondate = input("Enter a date in dd/mm/yyyy format: ").strip()
    try:
        tempondate = datetime.strptime(tempondate, '%d/%m/%Y').date()
    except ValueError as e:
        print(f'Not a valid date string, try again')
    previous_day = tempondate - timedelta(1)
    next_day = tempondate + timedelta(1)
    print(str(tempondate))
    print(f"{previous_day} : {temps.get(str(previous_day), 'no data available')}")
    print(f"{tempondate} : {temps.get(str(tempondate), 'no data available')}")
    print(f"{next_day} : {temps.get(str(next_day), 'no data available')}")

get_temps()


