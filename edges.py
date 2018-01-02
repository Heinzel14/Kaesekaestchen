from zeichner import *
from boxes import *
from player import *

edges = {}

class Edge:

	def __init__(self, Box, startPoint, endPoint):
		self.value = 1
		self.position = (startPoint, endPoint)
		self.edgeBoxes = [Box]
		edges[self.position] = self
		self.canvasObject = None

	def set_edge(self, Player):

		if self.value == 1:

			return

		else:

			self.value = 1
			canv.itemconfig(self.canvasObject, width=10, fill="red")

			for Box in self.edgeBoxes:

				Box.full_box_check(Player)



			return


	def unset_edge(self):

			self.value = 0



