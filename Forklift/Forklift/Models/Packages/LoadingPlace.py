from Models.MapElement import MapElement

class LoadingPlace(MapElement):
	def getPosition(self):
		return __position

	def getListOfPackages(self):
		return self.__listOfPackages

	def addPackage(self, package):
		self.__listOfPackages.append(package)

	def removePackage(self):
		return self.__listOfPackages.pop()

	def __init__(self, position, listOfPackages):
		self.__position = position
		self.__listOfPackages = listOfPackages