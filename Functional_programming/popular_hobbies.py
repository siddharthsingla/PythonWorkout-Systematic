from collections import Counter
def popular_hobbies(listofdicts):
    return Counter([hobby for dic in listofdicts for hobby in dic['hobbies']]).most_common(3)

listofhobbies = [{'name': 'firsr', 'hobbies':(1, 2, 3, 4)},{'name': 'second', 'hobbies':(1, 2, 3, 4)}, {'name': 'third', 'hobbies':(5, 1, 3, 4)}]

print(popular_hobbies(listofhobbies))