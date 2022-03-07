from Models.Position import Position
from Models.MapElement import MapElement

class Road(MapElement):

	def __init__(self, maxWeight, heightFromTheCeiling):
		self.__maxWeight = maxWeight
		self.__heightFromTheCeiling = heightFromTheCeiling

	def getMaxWeight(self):
		return self.__maxWeight

	def getHeightFromTheCeiling(self):
		return self.__heightFromTheCeiling

