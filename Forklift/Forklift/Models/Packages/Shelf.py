class Shelf:
	def getWidth(self):
		return self.__width
	
	def getDepth(self):
		return self.__depth

	def getHeight(self):
		return self.__height

	def putOnTheShelf(self, package):
		# układanie paczek, by było jak najwięcej miejsca na półce
		# jeżeli jest miejsce
		self.__listOfPackages.append(package)
		# dodajemy do blockedSpaces naszą paczkę

	def pullFromTheShelf(self, package):
		for p in self.__listOfPackages:
			if(package == p):
				return self.__listOfPackages.pop(package)
		return None

	def pullFromTheShelf(self):
		return self.__listOfPackages.pop()

	def __init__(self, width, depth, height):
		self.__width = width
		self.__depth = depth
		self.__height = height
		self.__blockedSpaces = []
		self.__listOfPackages = []
