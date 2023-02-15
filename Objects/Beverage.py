class Beverage():
    def __init__(self, name, temperature=75):
        self.name = name
        self.temp = temperature

def create_beverages():
    beverages = [Beverage('beer', 32), Beverage('pepsi', 34), Beverage('coke')]
    for beverage in beverages:
        print(beverage.name, beverage.temp)

create_beverages()