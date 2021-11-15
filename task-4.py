class Warehouse:
	pass


class Equipment:
	quantity = 0
	cost = 0


class Printer(Equipment):
	def __init__(self, quantity, cost, name, color, weight):
		self.quantity = quantity
		self.cost = cost
		self.name = name
		self.color = color
		self.weight = weight


class Scanner(Equipment):
	def __init__(self, quantity, cost, name, color, height):
		self.quantity = quantity
		self.cost = cost
		self.name = name
		self.color = color
		self.height = height


class Xerox(Equipment):
	def __init__(self, quantity, cost, name, color, width):
		self.quantity = quantity
		self.cost = cost
		self.name = name
		self.color = color
		self.width = width


# printer = Printer(1, 2, 'Printer', 'white', 1000)
# scanner = Scanner(1, 3, 'Scanner', 'black', 30)
# xerox = Xerox(1, 1, 'Xerox', 'red', 40)
