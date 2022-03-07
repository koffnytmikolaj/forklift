
class Forklift:

	def getPosition(self):
		return self.__position

	def getWheelNumber(self):
		return self.__wheelNumber

	def getDriveMotor(self):
		return self.__driveMotor

	def getLiftingMotor(self):
		return self.__liftingMotor

	def getLiftingCapacity(self):
		return self.__liftingCapacity

	def getLiftingHeight(self):
		return self.__liftingHeight

	def getMaxSpeed(self):
		return self.__maxSpeed

	def getAccumulator(self):
		return self.__accumulator

	def getWeight(self):
		return self.__weight

	def getProducer(self):
		return self.__producer

	def getMinHeight(self):
		return self.__minHeight

	def getMaxHeight(self):
		return self.__maxHeight

	def getWidth(self):
		return self.__width

	def getForkLength(self):
		return self.__forkLength

	def getProximitySensorsNumber(self):
		return self.__proximitySensorsNumber

	def getCamerasNumber(self):
		return self.__camerasNumber

	def __init__(self, position, wheelNumber, driveMotor, liftingMotor, liftingCapacity, liftingHeight, maxSpeed, accumulator, weight,
					 producer, minHeight, maxHeight, width, forkLength, proximitySensorsNumber, camerasNumber, forkliftMap):
		self.__position = position
		self.__wheelNumber = wheelNumber
		self.__driveMotor = driveMotor
		self.__liftingMotor = liftingMotor
		self.__liftingCapacity = liftingCapacity
		self.__liftingHeight = liftingHeight
		self.__maxSpeed = maxSpeed
		self.__accumulator = accumulator
		self.__weight = weight
		self.__producer = producer
		self.__minHeight = minHeight
		self.__maxHeight = maxHeight
		self.__width = width
		self.__forkLength = forkLength
		self.__proximitySensorsNumber = proximitySensorsNumber
		self.__camerasNumber = camerasNumber
		self.__forkliftMap = forkliftMap

	def showAll(self):
		print(
			f"""
Position: {self.__position.x},{self.__position.y}\n
Wheel Number: {self.__wheelNumber}\n
Drive Motor: type: {self.__driveMotor.getType()}, power: {self.__driveMotor.getPower()}kW\n
Lifting Motor: type: {self.__liftingMotor.getType()}, power: {self.__liftingMotor.getPower()}kW\n
Lifting Capacity: {self.__liftingCapacity}kg\n
Lifting Height: {self.__liftingHeight}mm\n
Max Speed: {self.__maxSpeed}km/h\n
Accumulator: capacity: {self.__accumulator.getCapacity()}Ah, voltage: {self.__accumulator.getVoltage()}V, weight: {self.__accumulator.getWeight()}kg\n
Weight: {self.__weight}kg\n
Producer: name: `{self.__producer.getName()}`, country: {self.__producer.getCountry()}\n
Min Height: {self.__minHeight}mm\n
Max Height: {self.__maxHeight}mm\n
Width: {self.__width}mm\n
Fork Length: {self.__forkLength}mm\n
Proximity Sensors Number: {self.__proximitySensorsNumber}\n
Cameras Number: {self.__camerasNumber}\n
			"""
		)
