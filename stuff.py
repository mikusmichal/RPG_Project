import os
from player import Player
from npc import NPC


def clear_screen():
    os.system('cls')


def spawn(name):
    x = NPC()
    x.name = name
    x.setup_name()
