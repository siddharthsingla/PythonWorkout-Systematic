def hex_to_decimal(hex_num):
    total = 0
    for i, digit in enumerate(reversed(hex_num)):
        total += (16**i) * int(digit, 16)
    return total

print(hex_to_decimal("ffff"))