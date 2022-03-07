from Models.MapElement import MapElement
class Locker(MapElement):
	def getPosition_0_0():
		return self.__position_0_0

	def getPosition_m_n():
		return self.__position_m_n
	
	def __init__(self, position_0_0, position_m_n, typeOfProduct, listOfShells):
		self.__position_0_0 = position_0_0
		self.__position_m_n = position_m_n
		self.__typeOfProduct = typeOfProduct
		self.__listOfShells = listOfShells