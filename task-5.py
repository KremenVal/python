class Warehouse:
	items = {'quantity': 0, 'printer': {}, 'scanner': {}, 'xerox': {}}

	def add_item(self, item):
		if item.name in self.items[item.type]:
			self.items[item.type][item.name][len(self.items[item.type][item.name])] = {
				'cost': item.cost, 'produced': item.country
			}
		else:
			self.items[item.type][item.name] = {0: {'cost': item.cost, 'produced': item.country}}

		self.items['quantity'] += 1

		return item.name + ' был добавлен на склад'

	def transfer(self, place, equipment_type, equipment_name, quantity):
		if self.items['quantity'] == 0:
			return 'Склад пустой, невозможно ничего передать.'
		else:
			if equipment_type in self.items:
				quantity_type = len(self.items[equipment_type])

				if quantity_type > 0:
					if equipment_name in self.items[equipment_type]:
						quantity_name = len(self.items[equipment_type][equipment_name])

						if quantity_name >= quantity:
							[self.items[equipment_type][equipment_name].popitem() for _ in range(quantity)]
							self.items['quantity'] -= quantity
							if len(self.items[equipment_type][equipment_name]) == 0:
								self.items[equipment_type].pop(equipment_name)
							return f'{equipment_name} в количестве {quantity} был перемешён в {place}.'
						else:
							return f'На складе есть только {quantity_name} из запрашуемых {quantity}.'
					else:
						return f'На складе нет техники {equipment_type} с таким именем как {equipment_name}.'
				else:
					return f'На складе есть только {quantity_type} {equipment_name}.'
			else:
				return f'На складе нет техники {equipment_type}.'


class Equipment:
	cost = 0
	owner = 'SpaceX'

	def __init__(self, cost, name):
		self.cost = cost
		self.name = name


class Printer(Equipment):
	type = 'printer'

	def __init__(self, cost, name, country):
		Equipment.__init__(self, cost, name)

		self.country = country


class Scanner(Equipment):
	type = 'scanner'

	def __init__(self, cost, name, country):
		Equipment.__init__(self, cost, name)

		self.country = country


class Xerox(Equipment):
	type = 'xerox'

	def __init__(self, cost, name, country):
		Equipment.__init__(self, cost, name)

		self.country = country


printer = Printer(2000, 'Printer', 'Russia')
scanner = Scanner(3000, 'Scanner', 'Ukraine')
xerox = Xerox(1000, 'Xerox', 'USA')
warehouse = Warehouse()
warehouse.add_item(printer)
warehouse.add_item(printer)
warehouse.add_item(scanner)
warehouse.add_item(scanner)
print(warehouse.items)
print(warehouse.transfer('tyda', 'printer', 'Printer', 1))
print(warehouse.transfer('tyda', 'printer', 'Printer', 3))
print(warehouse.items)
print(warehouse.transfer('tyda', 'printer', 'Printer', 1))
print(warehouse.items)
print(warehouse.transfer('tyda', 'scanner', 'Scanner', 1))
print(warehouse.items)
print(warehouse.transfer('tyda', 'scanner', 'Scanner', 1))
print(warehouse.items)
