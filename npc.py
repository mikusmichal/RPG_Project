import random


class NPC:
    def __init__(self, strength, perception, endurance, charisma, intelligence, agility, luck, weapon):
        self.strength = 1 + random.randint(0, strength)
        self.perception = 1 + random.randint(0, perception)
        self.endurance = 1 + random.randint(0, endurance)
        self.charisma = 1 + random.randint(0, charisma)
        self.intelligence = 1 + random.randint(0, intelligence)
        self.agility = 1 + random.randint(0, agility)
        self.luck = 1 + random.randint(0, luck)
        self.x = random.randint(1, 2)
        self.y = random.randint(1, 2)
        self.location = (self.x, self.y)
        self.health = 5 + self.endurance
        self.weapon = weapon
        self.name = ''

    def view_stats(self):
        print("S:" + str(self.strength))
        print("P:" + str(self.perception))
        print("E:" + str(self.endurance))
        print("C:" + str(self.charisma))
        print("I:" + str(self.intelligence))
        print("A:" + str(self.agility))
        print("L:" + str(self.luck))
        print("Radroach location is " + str(self.x) + ", " + str(self.y) + ")")





