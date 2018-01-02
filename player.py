players = []


class Player:

    def __init__(self, name, color):
        self.name = name
        players.append(self)
        self.points = 0

    def add_point(self):
        self.points += 1
        #Spieler muss nochmal dran sein
        return
