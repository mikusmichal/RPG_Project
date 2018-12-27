from player import Player
from actions import MoveNorthAction, MoveSouthAction, MoveEastAction, MoveWestAction, ShowStats
from stuff import clear_screen, create_radroach

if __name__ == "__main__":

    actions = [
        MoveNorthAction(),
        MoveSouthAction(),
        MoveEastAction(),
        MoveWestAction(),
        ShowStats
    ]
    player = Player(weapon='', x=0, y=0)
    create_radroach(name='radroach')
    winning = False

    while not winning:
        player.location = (player.x, player.y)
        print("Your location is: " + str(player.location))
        user_input = input("\n")
        clear_screen()

        words = user_input.split(' ')
        action_input = words[0]
        available_action = [a for a in actions if a.name == action_input]

        action = available_action[0]
        action.perform(player, location=player.location)

