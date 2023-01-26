def dict_partition(d, fn):
    d1 = {}
    d2 = {}
    for key, value in d.items():
        if fn(key):
            d1[key] = value
        else:
            d2[key] = value

def fn(arg):
    pass