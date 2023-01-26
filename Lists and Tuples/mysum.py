def mysum(*elements):
    total = elements[0]
    for element in elements[1:]:
        total += element

    return total

print(mysum("abc", 123))