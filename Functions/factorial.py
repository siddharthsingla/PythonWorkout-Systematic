def factorial(*args):
    output = args[0]
    for arg in args[1:]:
        output *= arg
    return output
print(factorial(5,4,3,2))