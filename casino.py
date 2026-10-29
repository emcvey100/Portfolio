#cassino
class Player:
    #To create player, give it a name, money and games played
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.games_played = []
    def __repr__(self):
        #printing player gives its name and amount of money
        return f"{self.name} has £{self.money} left.
    def add_money(money):
        self.money+=money

class Game:
    #To create game
    def __init__(self, cost, players, name):
        self.cost = cost
        self.name = name
        self.players = players
    def __repr__(self):
        #print
        return f"
