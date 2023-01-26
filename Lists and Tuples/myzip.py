def myzip(*args):
    output = []
    for i in range(len(args[0])):
        temp = []
        for arg in args:
            temp.append(arg[i])
        output.append(tuple(temp))
    return output

def myzipv2(*args):
    return [tuple([arg[i] for arg in args]) for i in range(len(min(args, key=len)))]

print(myzipv2([10, 20,30], 'abc'))