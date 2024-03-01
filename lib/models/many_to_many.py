class Tokens:
    def __init__(self, name, package, price):
        self.name = name

class Player:
    def __init__(self, name):
        self.name = name

class Purchase:
    def __init__(self, player, package, price):
        self.player = player
        self.package = package
        self.price = price
        

