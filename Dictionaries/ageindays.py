from datetime import date, datetime, timedelta
PEOPLE = {'Reuven': date.fromisoformat('1970-07-14'),
          'Atara': date.fromisoformat('2000-12-16'),
          'Shikma': date.fromisoformat('2002-12-17'),
          'Amotz': date.fromisoformat('2005-10-31')
          }
def age_in_days():
    member = input("Enter a family member's name in ISO format: ").strip()
    print(type(date.today()))
    print(type(datetime.today().isoformat()))
    print((date.today() - PEOPLE[member]).days)

age_in_days()