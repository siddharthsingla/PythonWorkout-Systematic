"""Ask the user to enter integers, separated by spaces. From this input, create a
dict whose keys are the factors for each number, and the values are lists containing
those of the users’ integers that are multiples of those factors"""
from collections import defaultdict
def factors():
    numbers = input("Enter numbers: ").strip()
    output = defaultdict(list)
    factor_list = set()
    for number in numbers.split():
        number = int(number)
        for i in range(2, number + 1):
            if number % i == 0:
                output[i].append(number)

    print(output)

factors()