from edges import *

Boxes = {}

#This class represents the boxes of the game "Käsekästchen". By default all the edges are set to 1.
#When created the object needs it's coordinates (which need to be unique) and will look for neighbours and adapt the "edges" and "neighbours" dictionary of the neighbour and it self.
#It will add itself to the global Boxes dictionary with it's coordinates as the key.
#The function set_edge sets the given edge from 0 to one and also updates the edge of the corresponding neighbour.
#The output is 0 if the edge is already set, 1 if the edge was set but it was not the last one and 2 if the edge was set and all edges are 1 now


class Box:

    def __init__(self, coordinates):

        (self.x, self.y) = coordinates
        self.name = "Box" + str(self.x) + str(self.y)
        self.neighbours = {"right": None, "left": None, "up": None, "down": None}
        self.boxEdges = {"right": None, "left": None, "up": None, "down": None}
        Boxes[(self.x, self.y)] = self

        if ((self.x+1), self.y) in Boxes:

            Boxes[((self.x+1), self.y)].neighbours["left"] = self
            self.neighbours["right"] = Boxes[((self.x+1), self.y)]
            self.boxEdges["right"] = self.neighbours["right"].boxEdges["left"]
            self.boxEdges["right"].unset_edge()
            self.boxEdges["right"].edgeBoxes.append(self)

        else:
            self.boxEdges["right"] = Edge(self, (self.x + 1, self.y), (self.x + 1, self.y + 1))

        if ((self.x-1), self.y) in Boxes:

            Boxes[((self.x-1), self.y)].neighbours["right"] = self
            self.neighbours["left"] = Boxes[((self.x - 1), self.y)]
            self.boxEdges["left"] = self.neighbours["left"].boxEdges["right"]
            self.boxEdges["left"].unset_edge()
            self.boxEdges["right"].edgeBoxes.append(self)


        else:
            self.boxEdges["left"] = Edge(self, (self.x, self.y), (self.x, self.y + 1))

        if (self.x, (self.y+1)) in Boxes:

            Boxes[(self.x, (self.y+1))].neighbours["down"] = self
            self.neighbours["up"] = Boxes[(self.x, (self.y+1))]
            self.boxEdges["up"] = self.neighbours["up"].boxEdges["down"]
            self.boxEdges["up"].unset_edge()
            self.boxEdges["right"].edgeBoxes.append(self)


        else:
            self.boxEdges["up"] = Edge(self, (self.x, self.y+1), (self.x+1, self.y+1))

        if (self.x, (self.y-1)) in Boxes:

            Boxes[(self.x, (self.y-1))].neighbours["up"] = self
            self.neighbours["down"] = Boxes[(self.x, (self.y-1))]
            self.boxEdges["down"] = self.neighbours["down"].boxEdges["up"]
            self.boxEdges["down"].unset_edge()
            self.boxEdges["right"].edgeBoxes.append(self)

        else:
            self.boxEdges["down"] = Edge(self, (self.x, self.y), (self.x+1, self.y))

    def full_box_check(self, Player):

        i=0

        for key in self.boxEdges:
            i += self.boxEdges[key].value

        if i == 4:
            Player.add_point()
            #hier muss das entsprechende Kästchen dann für den Spieler ausgemalt werden

        return




