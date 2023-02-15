def join_numbers(string):
    return ','.join([f"{num}" for num in string if 0 <= num < 10])
