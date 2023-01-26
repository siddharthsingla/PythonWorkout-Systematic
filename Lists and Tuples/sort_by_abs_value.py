def sort_by_abs_value(listofnumbers):
    return sorted(listofnumbers, key=abs)

print(sort_by_abs_value([1,2,3,4,-1,-2,-10,2]))