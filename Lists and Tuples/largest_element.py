def largest_element(seq):
    if not seq:
        return None
    largest = seq[0]
    for x in seq:
        if x > largest:
            largest = x

    return largest

print(largest_element([1,2,3,4]))