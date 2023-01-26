PEOPLE = [{'first':'Reuven', 'last':'Lerner','email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin','email':'president@kremvax.ru'}
]

import operator
def alphabetize_names():
    print(sorted(PEOPLE, key=lambda x: (x['last'], x['first'])))

def alphabetize_namesv2():
    print(sorted(PEOPLE, key=operator.itemgetter('last', 'first')))

alphabetize_namesv2()
