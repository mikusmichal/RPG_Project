import random


class NPC:
    name = ''
    strength = 1
    perception = 1
    endurance = 1
    charisma = 1
    intelligence = 1
    agility = 1
    luck = 1
    health = 1
    weapon = ''
    x = 0
    y = 0
    location = (x, y)

    def view_stats(self):
        print("S:" + str(self.strength))
        print("P:" + str(self.perception))
        print("E:" + str(self.endurance))
        print("C:" + str(self.charisma))
        print("I:" + str(self.intelligence))
        print("A:" + str(self.agility))
        print("L:" + str(self.luck))
        print("Radroach location is " + str(x) + ", " + str(y) + ")")

    def setup_name(self):
        if self.name == 'radroach':
            NPC.setup_radroach()

    def setup_radroach(self):
        self.strength = 1 + random.randint(0, 1)
        self.perception = 1 + random.randint(0, 1)
        self.endurance = 1 + random.randint(0, 1)
        self.charisma = 1 + random.randint(0, 1)
        self.intelligence = 1 + random.randint(0, 1)
        self.agility = 1 + random.randint(0, 1)
        self.luck = 1
        self.x = 1 + random.randint(0, 1)
        self.y = 1 + random.randint(0, 1)
        self.location = self.x + self.y
