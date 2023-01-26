import decimal
def fp_add(f1, f2):
    return (decimal.Decimal(f1) + decimal.Decimal(f2))

print(fp_add(0.1, 0.2))