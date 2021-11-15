class Warehouse:
	pass


class Equipment:
	cost = 0


class Printer(Equipment):
	def __init__(self, cost, name, weight):
		self.cost = cost
		self.name = name
		self.weight = weight


class Scanner(Equipment):
	def __init__(self, cost, name, height):
		self.cost = cost
		self.name = name
		self.height = height


class Xerox(Equipment):
	def __init__(self, cost, name, width):
		self.cost = cost
		self.name = name
		self.width = width


# printer = Printer(2000, 'Printer', 1000)
# scanner = Scanner(3000, 'Scanner', 30)
# xerox = Xerox(1000, 'Xerox', 40)
# print(printer, scanner, xerox)
