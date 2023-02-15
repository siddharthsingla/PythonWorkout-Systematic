def flatten_odd_only(listoflists):
    return [x for element in listoflists for x in element if x%2]

#print(flatten_odd_only([[1,2], [3,4]]))

def flatten_odd_onlyv2(listoflists):
    if len(listoflists) == 0:
        print("1", listoflists)
        return listoflists
    if isinstance(listoflists[0], list):
        print("2", listoflists)
        return flatten_odd_onlyv2(listoflists[0]) + flatten_odd_onlyv2(listoflists[1:])
    elif listoflists[0] % 2:
        print("3", listoflists[:1])
        return listoflists[:1] + flatten_odd_onlyv2(listoflists[1:])
    else:
        print("4", listoflists)
        return flatten_odd_onlyv2(listoflists[1:])

print(flatten_odd_onlyv2([[1,2], [3,4]]))
