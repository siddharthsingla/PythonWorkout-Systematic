def mysum(listofnumbers, start_value=0):
    output = start_value
    for num in listofnumbers:
        output += num
    return output

print(mysum([1,2,4], 3))
