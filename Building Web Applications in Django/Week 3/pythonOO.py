class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, person):
        self.name = person
        print(self.name, 'constructed! :D')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)
    
    def __del__(self):
        print(self.name, 'destructed!! D:')

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points:', self.points)


# Tests
print(dir(PartyAnimal))
print(dir(FootballFan))

s = PartyAnimal('Sally')
print(dir(s))
s.party()
s.party()
s = 42
print(dir(s))

j = FootballFan('Jim')
print(dir(j))
j.party()
j.touchdown()