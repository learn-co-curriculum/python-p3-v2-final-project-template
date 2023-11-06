from models.__init__ import CURSOR, CONN

class Game:
    all_games = []

    def __init__(self, name, id=None):
        self.name = name
        Game.all.append(self)

    def __repr__(self):
        return f"{self.name}"