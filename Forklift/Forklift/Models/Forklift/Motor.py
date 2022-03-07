from Enums.MotorType import MotorType

class Motor:

	def __init__(self, type, power):
		self.__type = type
		self.__power = power

	def getType(self):
		return self.__type

	def getPower(self):
		return self.__power