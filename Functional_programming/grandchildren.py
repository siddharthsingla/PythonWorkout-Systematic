import operator
def get_grandchildren(family):
    print([child['name'] for child in sorted([x for key, value in family.items() for x in value], key=operator.itemgetter("age"))])



family = {'A': [{"name":'B', "age": 5}, {"name":'C', "age": 4}, {"name": 'D', "age": 8}], 'E': [{"name": 'F', "age": 10}, {"name": 'G', "age": 9}]}
get_grandchildren(family)