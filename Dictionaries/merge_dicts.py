def merge_dicts(*args):
    output = {}
    for arg in args:
        for key, value in arg.items():
            output[key] = value
    return output
d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(merge_dicts(d1,d2))