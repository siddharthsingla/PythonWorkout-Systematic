

def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiply(x, y):
    return x * y
    return operators[op]
def calc(pfn):
    params = pfn.split()
    op = params[0]
    output = int(params[1])
    for x in params[2:]:
        output = operators[op](output, int(x))
    return output

operators = {"+": plus, "-":minus, "*":multiply}
print(calc("* 1 2 3"))