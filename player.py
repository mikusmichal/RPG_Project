import random

class Player:
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

    def setup_stats(self):
        self.strength = 1 + random.randint(0, 2)
        self.perception = 1 + random.randint(0, 2)
        self.endurance = 1 + random.randint(0, 2)
        self.charisma = 1 + random.randint(0, 2)
        self.intelligence = 1 + random.randint(0, 2)
        self.agility = 1 + random.randint(0, 2)
        self.luck = 1 + random.randint(0, 1)
