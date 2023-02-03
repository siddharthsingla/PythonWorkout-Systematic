def before_after(fp, before, after):
    temp = str(fp)
    i = temp.index(".")
    return float(temp[i - before: i+after+1])

print(before_after(1234.56789, 2, 4))