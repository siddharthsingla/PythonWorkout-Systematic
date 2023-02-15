def dict_to_tuple(listofdicts):
    return [(key, value) for dic in listofdicts for key, value in dic.items()]
