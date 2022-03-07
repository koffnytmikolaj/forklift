from Models.MapElement import MapElement

class Blockade(MapElement):
	def getPosition(self):
		return self.__position

	def __init__(self, position):
		self.__position = position
