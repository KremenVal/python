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


def get_int(txt):
	while True:
		number = input(txt)

		if number.isdecimal():
			return int(number)
		else:
			print('Вы ввели не число.')


def list_warehouse(warhs):
	for key, value in warhs.items.items():
		if key == 'quantity':
			print(f'\nНа скаладе присутствует {value} оргтеники.')
		else:
			tmp_list = list(value.items())
			name = tmp_list[0][0]
			amount = len(tmp_list[0][1])

			print(f'Из них {amount} типа "{key}" с именем {name}.')


warehouse = Warehouse()
type_equipment = {
	'принтера': Printer,
	'сканера': Scanner,
	'ксерокса': Xerox,
}

for key, value in type_equipment.items():
	equipment = {
		'cost': get_int(f'Введите стоимость {key} - '),
		'name': input(f'Введите название {key} - '),
		'country': input(f'Введите страну производитель {key} - ')
	}

	amount_equipment = get_int(f'Введите количество {key}, которые вы хотите отправить на склад - ')

	for i in range(amount_equipment):
		warehouse.add_item(value(equipment['cost'], equipment['name'], equipment['country']))


while True:
	list_warehouse(warehouse)

	moving = {
		'place': input('Введите подразделение, куда хотите отправить оргтенику - '),
		'type': input('Введите тип оргтеники (printer/scanner/xerox) - '),
		'name': input('Введите имя оргтеники - '),
		'amount': get_int('Введите количество оргтеники для перемещения - '),
	}

	print(warehouse.transfer(moving['place'], moving['type'], moving['name'], moving['amount']))

	stop = input('Введите команду "stop" для прекращения перемещения оргтеники - ')

	if stop == 'stop':
		break
