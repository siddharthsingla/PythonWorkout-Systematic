

def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiply(x, y):
    return x * y
    return operators[op]
def calc(pfn):
    op, x, y = pfn.split()
    return operators[op](int(x), int(y))

operators = {"+": plus, "-":minus, "*":multiply}
print(calc("* 1 2"))