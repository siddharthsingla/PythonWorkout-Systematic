def flip_dict(dic):
    return {value: key for key, value in dic.items()}

print(flip_dict({'a':1, 'b':2, 'c':3}))