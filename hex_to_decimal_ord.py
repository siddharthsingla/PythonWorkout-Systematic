def hex_to_decimal():
    hex_input = input("Enter a hexadecimal number: ")
    decimal_number = 0
    for i, digit in enumerate(reversed(hex_input)):
        if ord(digit) <= 57 and ord(digit) >= 48:
            num = ord(digit) - 48
        elif ord(digit) <= 102 and ord(digit) >= 97:
            num = ord(digit) - 87

        decimal_number += (16**i) * num
    return decimal_number

print(hex_to_decimal())