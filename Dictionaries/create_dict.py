def create_dict(*args):
    args = list(args)
    output = {}
    while args:
        output[args.pop(0)] = args.pop(1)
    return output

def create_dictv2(*args):
    output = {}
    while args:
        output[args[0]] = args[1]
        args = args[2:]
    return output

print(create_dictv2(1,2,3,4))