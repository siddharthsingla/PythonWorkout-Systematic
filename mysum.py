def mysum(*args):
    output = 0
    for arg in args:
        output += arg
    return output

print(mysum(1,2,3,4,5,6))