def combine_dicts(listofdicts):
    output = {}
    for dic in listofdicts:
        for k, v in dic.items():
            if k in output:
                if type(output[k]) == list:
                    output[k].append(v)
                else:
                    output[k] = [output[k], v]
            else:
                output[k] = v
    return output

def combine_dictsv2(listofdicts):
    output = {}
    for dic in listofdicts:
        for k, v in dic.items():
            if k in output:
                try:
                    output[k].append(v)
                except AttributeError:
                    output[k] = [output[k], v]
            else:
                output[k] = v
    return output
print(combine_dictsv2([{'a': 1}, {'b':2}, {'a':3}, {'a':4}]))