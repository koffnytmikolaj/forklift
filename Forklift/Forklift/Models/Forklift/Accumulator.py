
class Accumulator:
	def __init__(self, capacity, voltage, weight):
		self.__capacity = capacity
		self.__voltage = voltage
		self.__weight = weight

	def getCapacity(self):
		return self.__capacity

	def getVoltage(self):
		return self.__voltage

	def getWeight(self):
		return self.__weight
