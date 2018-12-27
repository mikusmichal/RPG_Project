from player import Player


class Action:
    name = None

    def perform(self, player: Player, location):
        pass


class ShowStats(Action):
    name = 'mystats'

    def perform(self, player: Player, location):
        player.view_stats()


class MoveNorthAction(Action):
    name = 'north'

    def perform(self, player: Player, location):
        player.y += 1


class MoveSouthAction(Action):
    name = 'south'

    def perform(self, player: Player, location):
        player.y -= 1


class MoveEastAction(Action):
    name = 'east'

    def perform(self, player: Player, location):
        player.x += 1


class MoveWestAction(Action):
    name = 'west'

    def perform(self, player: Player, location):
        player.x -= 1