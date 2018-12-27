import os
from player import Player
from npc import NPC


def clear_screen():
    os.system('cls')


def create_radroach(name):
    x = NPC(strength=1, perception=0, endurance=2, charisma=1, intelligence=1, agility=1, luck=0, weapon='')
    x.name = name
