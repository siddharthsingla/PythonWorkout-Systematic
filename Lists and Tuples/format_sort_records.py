PEOPLE = [('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)]
def format_sort_records():
    for person in PEOPLE:
        print(f"{person[1]:<20} {person[0]:<20} {person[2]:>5.2f}")

import operator

def format_sort_recordsv2():
    output = []
    template = "{1:10} {0:10} {2:5.2f}"
    for person in sorted(PEOPLE, key=operator.itemgetter(1,0)):
        output.append(template.format(*person))
    return output
print('\n'.join(format_sort_recordsv2()))