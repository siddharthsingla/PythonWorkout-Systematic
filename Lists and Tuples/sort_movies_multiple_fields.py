import operator

def sort_movies_multiple_fields(listofmovies):
    sortby = input("Enter criteria of sorting movies: ")
    sortby = sortby.strip().split(",")
    template = "{0:30} {1:3} {2:15}"
    sortbydic = {'title': 0, 'length': 1, 'director': 2}
    output = []
    if all(field in sortbydic for field in sortby):

        sorted_movies = sorted(listofmovies, key=operator.itemgetter(*[sortbydic[x] for x in sortby]))
        for movie in sorted_movies:
            output.append(template.format(*movie))
    return output
MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Parasite', 122, 'Dong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]
print(sort_movies_multiple_fields(MOVIES))


