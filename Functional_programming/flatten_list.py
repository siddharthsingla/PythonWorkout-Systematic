def flatten_list(listoflist):
    return [second_level for first_level in listoflist for second_level in first_level]

#print(flatten_list([[1,2], [3,4]]))

output = []
def flatten_n_level_list(listoflists):
    global output
    for element in listoflists:
        if type(element) != list:
            output.append(element)
        else:
            flatten_n_level_list(element)

#flatten_n_level_list([0, [1,2], [3,4, [5, [6, 7]]]])
#print(output)

def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

print(flatten([0, [1,2], [3,4, [5, [6, 7]]]]))