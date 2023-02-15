class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops():
    scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
    return scoops
class Bowl():
    def __init__(self):
        self.scoops = []
    def add_scoop(self, *flavors):
        for scoop in flavors:
            self.scoops.append(scoop)
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)
scoops = create_scoops()
bowl = Bowl()
bowl.add_scoop(scoops[1])
bowl.add_scoop(scoops[0], scoops[2])
print(bowl)