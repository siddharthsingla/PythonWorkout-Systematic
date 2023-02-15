def join_numbers(numbers):
    return ",".join(f"{number}" for number in numbers)

print(join_numbers(range(15)))