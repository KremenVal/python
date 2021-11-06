class Worker:
	name = ''
	surname = ''
	position = ''
	_income = {}

	def __init__(self, name, surname, position, income):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = income


class Position(Worker):
	def get_full_name(self):
		return self.name + ' ' + self.surname

	def get_total_income(self):
		return sum(map(lambda item: item, [value for value in self._income.values()]))


position_1 = Position('Иван', 'Иванов', 'IT-шник', {'wage': 150000, 'bonus': 10000})
print(position_1.get_full_name())
print(position_1.get_total_income())
