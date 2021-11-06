class Car:
	speed = 0
	color = ''
	name = ''
	is_police = True

	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		return 'Машина поехала'

	def stop(self):
		return 'Машина остановилась'

	def turn(self, direction):
		return f"Машина повернула на {direction}"

	def show_speed(self):
		return self.speed


class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			return 'Превышение скорости'
		else:
			return Car.show_speed(self)


class SportCar(Car):
	pass


class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			return 'Превышение скорости'
		else:
			return Car.show_speed(self)


class PoliceCar(Car):
	pass


townCar_1 = TownCar(65, 'red', 'toyota', False)
townCar_2 = TownCar(55, 'red', 'toyota', False)
sportCar = SportCar(300, 'yellow', 'lamborgini', False)
workCar_1 = WorkCar(50, 'black', 'nissan', False)
workCar_2 = WorkCar(35, 'black', 'nissan', False)
policeCar = PoliceCar(70, 'white', 'mercedes', True)
print(townCar_1.speed)
print(townCar_1.color)
print(townCar_1.name)
print(townCar_1.is_police)
print(townCar_1.show_speed())
print()
print(townCar_2.speed)
print(townCar_2.color)
print(townCar_2.name)
print(townCar_2.is_police)
print(townCar_2.show_speed())
print()
print(sportCar.speed)
print(sportCar.color)
print(sportCar.name)
print(sportCar.is_police)
print(sportCar.show_speed())
print()
print(workCar_1.speed)
print(workCar_1.color)
print(workCar_1.name)
print(workCar_1.is_police)
print(workCar_1.show_speed())
print()
print(workCar_2.speed)
print(workCar_2.color)
print(workCar_2.name)
print(workCar_2.is_police)
print(workCar_2.show_speed())
print()
print(policeCar.speed)
print(policeCar.color)
print(policeCar.name)
print(policeCar.is_police)
print(policeCar.show_speed())
