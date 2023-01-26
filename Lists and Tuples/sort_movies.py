import operator

def sort_movies(listofmovies, sortby):
    template = "{0:30} {1:3} {2:15}"
    output = []
    sortbydic = {'title': 0, 'director': 1, 'length': 2}
    for movie in sorted(listofmovies, key=operator.itemgetter(sortbydic[sortby])):
        output.append(template.format(*movie))
    return output

MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]
print(sort_movies(MOVIES, 'title'))