class Producer:
	def __init__(self, name, country):
		self.__name = name
		self.__country = country

	def getName(self):
		return self.__name

	def getCountry(self):
		return self.__country

	def changeName(self, name):
		self.__name = name