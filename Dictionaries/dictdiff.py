from collections import defaultdict
def dictdiff(d1, d2):
    output = {}
    for k in list(d1.keys() | d2.keys()):
        if d1.get(k) != d2.get(k):
            output[k] = [d1.get(k), d2.get(k)]

    return output
d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}

print(dictdiff(d1, d2))
print(dictdiff(d1, d1))

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3, d4))