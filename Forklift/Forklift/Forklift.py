from Models.Forklift.Forklift import Forklift
from Models.Forklift.Motor import Motor
from Models.Position import Position
from Models.Forklift.Accumulator import Accumulator
from Models.Forklift.Producer import Producer
from Models.Packages.Package import Package
from Models.Packages.LoadingPlace import LoadingPlace
from Models.Packages.Locker import Locker
from Models.Packages.Shelf import Shelf
from Models.Blockade import Blockade
from Models.Road import Road
from Enums.MotorType import MotorType
from Enums.Country import Country
from Enums.TypeOfProduct import TypeOfProduct


def createLoadingPlace():
	position = Position(0, 0)
	listOfPackages = [
		Package(30, 20, TypeOfProduct.food.name),
		Package(20, 40, TypeOfProduct.medicines.name),
		Package(30, 20, TypeOfProduct.building_materials.name),
		Package(40, 50, TypeOfProduct.food.name)
	]
	return LoadingPlace(position, listOfPackages)

def createLockerList():
	return [
		Locker(Position(3000, 1200), Position(4200, 5000), TypeOfProduct.food.name, [
			Shelf(1900, 600, 600),
			Shelf(1900, 600, 600)
		]),
		Locker(Position(6100, 1500), Position(7300, 7000), TypeOfProduct.building_materials.name, [
			Shelf(1500, 600, 600),
			Shelf(1500, 600, 600),
			Shelf(1500, 600, 600),
			Shelf(1500, 600, 1200)
		]),
		Locker(Position(800, 6100), Position(5500, 7300), TypeOfProduct.medicines.name, [
			Shelf(1100, 600, 600),
			Shelf(1100, 600, 600),
			Shelf(1100, 600, 600),
			Shelf(1100, 600, 600),
			Shelf(1100, 600, 1200),
			Shelf(1100, 600, 1200),
			Shelf(1100, 600, 1200),
			Shelf(1100, 600, 1200),
		])
	]

def createBlockadeList():
	return [
		Blockade(Position(3500, 600))
	]

def setLoadingPlace(forkliftMap):
	loadingPlace = createLoadingPlace()
	x = loadingPlace.getPosition().x
	y = loadingPlace.getPosition().y
	forkliftMap[x, y] = loadingPlace

def setLockerList(forkliftMap):
	lockerList = createLockerList()
	for locker in lockerList:
		for yPosition in range(locker.getPosition_0_0().y, locker.getPosition_m_n().y):
			for xPosition in range(locker.getPosition_0_0().x, locker.getPosition_m_n().x):
				forkliftMap[xPosition, yPosition] = locker

def setBlockadeList(forkliftMap):
	blockadeList = createBlockadeList()
	for blockade in blockadeList:
		forkliftMap[blockade.getPosition().x, blockade.getPosition().y] = blockade

def createMap():
	mapX = [0, 8000]
	mapY = [0,8000]
	forkliftMap = []
	#forkliftMap = [[Road(2500, 10000) for xPosition in range(mapX[0], mapX[1])] for yPosition in range(mapY[0], mapY[1])]
	#setLoadingPlace(forkliftMap)
	#setLockerList(forkliftMap)
	#setBlockadeList(forkliftMap)

	return forkliftMap

def createForklift(forkliftMap):
	position = Position(1000, 3000)
	wheelsNumber = 3
	driveMotor = Motor(MotorType.electric.name, 3.0)
	liftingMotor = Motor(MotorType.electric.name, 5.7)
	liftingCapacity = 1200
	liftingHeight = 5400
	maxSpeed = 12
	accumulator = Accumulator(300, 24, 230)
	weight = 1890
	producer = Producer("Still", Country.Germany.name)
	minHeight = 2137
	maxHeight = 4280
	width = 1337
	forkLength = 1150
	proximitySensorsNumber = 8
	camerasNumber = 4

	return Forklift(position, wheelsNumber, driveMotor, liftingMotor, liftingCapacity, liftingHeight, maxSpeed, accumulator, weight,
					 producer, minHeight, maxHeight, width, forkLength, proximitySensorsNumber, camerasNumber, forkliftMap)

def main():
	
	forkliftMap = createMap()
	forklift = createForklift(forkliftMap)
	forklift.showAll()

if __name__ == "__main__":
	main()
