from tkinter import *

edges = {}
Boxes = {}
players = []
rectangles = []

class Player:

	def __init__(self, name, color):

		self.name = name
		players.append(self)
		self.points = 0
		self.color = color

	def add_point(self):
		self.points += 1
		return

Player2 = Player("Achim", "red")
Player1 = Player("Momo", "blue")
currentPlayer = Player1

class Edge:
	def __init__(self, Box, startPoint, endPoint):
		self.value = 1
		self.position = (startPoint, endPoint)
		self.edgeBoxes = [Box]
		edges[self.position] = self
		self.canvasObject = None

	def set_edge(self):
		global currentPlayer
		i=0

		if self.value == 1:

			return

		else:

			self.value = 1
			canv.itemconfig(self.canvasObject, width=10, fill="red")

			for Box in self.edgeBoxes:
				i += Box.full_box_check()

		if i > 0:
			return

		else:
			if currentPlayer == Player1:
				currentPlayer = Player2
			else:
				currentPlayer=Player1

	def unset_edge(self):

			self.value = 0



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
			self.boxEdges["left"].edgeBoxes.append(self)


		else:
			self.boxEdges["left"] = Edge(self, (self.x, self.y), (self.x, self.y + 1))

		if (self.x, (self.y+1)) in Boxes:

			Boxes[(self.x, (self.y+1))].neighbours["down"] = self
			self.neighbours["up"] = Boxes[(self.x, (self.y+1))]
			self.boxEdges["up"] = self.neighbours["up"].boxEdges["down"]
			self.boxEdges["up"].unset_edge()
			self.boxEdges["up"].edgeBoxes.append(self)


		else:
			self.boxEdges["up"] = Edge(self, (self.x, self.y+1), (self.x+1, self.y+1))

		if (self.x, (self.y-1)) in Boxes:

			Boxes[(self.x, (self.y-1))].neighbours["up"] = self
			self.neighbours["down"] = Boxes[(self.x, (self.y-1))]
			self.boxEdges["down"] = self.neighbours["down"].boxEdges["up"]
			self.boxEdges["down"].unset_edge()
			self.boxEdges["down"].edgeBoxes.append(self)

		else:
			self.boxEdges["down"] = Edge(self, (self.x, self.y), (self.x+1, self.y))

	def full_box_check(self):

		i=0
		global currentPlayer

		for key in self.boxEdges:
			i += self.boxEdges[key].value

		if i == 4:
			currentPlayer.add_point()
			rectangles.append(canv.create_rectangle(20+self.x*50, 20+self.y*50, 20+(self.x+1)*50, 20+(self.y+1)*50, fill = currentPlayer.color))
			#hier muss das entsprechende Kästchen dann für den Spieler ausgemalt werden
			return 1

		return 0



root = Tk()
canv = Canvas(root, width=900, height=900)

def onObjectClick(event):
	object = event.widget.find_closest(event.x, event.y)
	(x1, y1, x2, y2) = canv.coords(object)
	#quick and dirty
	edges[((((x1+50)-20)/50-1,((y1+50)-20)/50-1),(((x2+50)-20)/50-1,((y2+50)-20)/50-1))].set_edge()
	canv.itemconfig(player1Text, text=Player1.name + " points:"+ str(Player1.points))
	canv.itemconfig(player2Text, text=Player2.name + " points:" + str(Player2.points))
	canv.itemconfig(currentPlayerText, text=currentPlayer.name + " it's your turn!", fill = currentPlayer.color)

	if Player1.points + Player2.points == len(Boxes):

		if Player2.points > Player1.points:
			canv.itemconfig(currentPlayerText, text="Congratulation " + Player1.name + " you won!")

		elif Player2.points < Player1.points:
			canv.itemconfig(currentPlayerText, text="Congratulation " + Player1.name +", " + Player2.name +" let you win!")

		else :
			canv.itemconfig(currentPlayerText, text="Booooring it's a tie.....")






for i in range(4):
	for j in range(4):
		Boxes[(i, j)] = Box((i, j))

for position in edges:

	((x1,y1), (x2,y2)) = position
	edges[position].canvasObject = canv.create_line(20+x1*50, 20+y1*50, 20+x2*50, 20+y2*50, width=5)
	canv.tag_bind(edges[position].canvasObject, '<ButtonPress-1>', onObjectClick)
	if edges[position].value == 1:
		canv.itemconfig(edges[position].canvasObject, width=10, fill="red")

currentPlayerText = canv.create_text(350, 600, text= currentPlayer.name + " it's your turn!", fill = "red", font = 40)
player1Text = canv.create_text(700, 100, text= Player1.name + " points: "+ str(Player1.points))
player2Text = canv.create_text(700, 300, text=Player2.name + " points: "+ str(Player1.points))

canv.pack()
print(currentPlayer.name + " Points:" + str(currentPlayer.points))
root.mainloop()
