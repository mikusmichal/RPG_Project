import random


class Player:
    def __init__(self, weapon, x, y):
        self.strength = random.randint(1, 2)
        self.perception = random.randint(1, 2)
        self.endurance = random.randint(1, 2)
        self.charisma = random.randint(1, 2)
        self.intelligence = random.randint(1, 2)
        self.agility = random.randint(1, 2)
        self.luck = random.randint(1, 2)
        self.x = x
        self.y = y
        self.location = (x, y)
        self.health = 10 + 2*self.endurance
        self.weapon = weapon

    def view_stats(self):
        print("S:" + str(self.strength))
        print("P:" + str(self.perception))
        print("E:" + str(self.endurance))
        print("C:" + str(self.charisma))
        print("I:" + str(self.intelligence))
        print("A:" + str(self.agility))
        print("L:" + str(self.luck))
        print("HP:" + str(self.health))


