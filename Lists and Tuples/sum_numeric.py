def sum_numeric(*numbers):
    return sum(int(number) for number in numbers if to_int(number))

def to_int(number):
    try:
        x = int(number)
    except:
        return False
    return True

print(sum_numeric(10, 20, 'a', '30','bcd'))
