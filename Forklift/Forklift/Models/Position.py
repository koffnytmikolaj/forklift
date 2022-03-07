
class Position:

	def changePosition(self, x, y):
		self.x = x
		self.y = y

	def __init__(self, x, y):
		self.changePosition(x, y)
