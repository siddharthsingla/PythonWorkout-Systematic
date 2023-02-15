def area_code(phone_numbers):
    return [new_number(number) for number in phone_numbers]

def new_number(number):
    xxx, yyy, zzzz = number.split("-")
    if yyy[0] in "012345":
        return f"{int(xxx) + 1}-{yyy}-{zzzz}"
    else:
        return number

print(area_code(['123-456-7890', '123-333-4444', '123-777-8888']))