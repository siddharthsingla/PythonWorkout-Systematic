def sum_numbers():
    numbers = input("Enter a string of numbers: ")
    print(sum(int(number) for number in numbers.split() if number.isdigit()))

def sum_numbersv2():
    numbers = input("Enter a string of numbers: ")
    print(sum(int(number) for number in numbers.split() if if_number(number)))

def if_number(number):
    try:
        int(number)
        return True
    except:
        return False
sum_numbersv2()