class MyDivisionByZero(Exception):
	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None

	def __str__(self):
		if self.message:
			return self.message
		else:
			return 'MyDivision By Zero'


a, b = int(input('Введите число: ')), int(input('Введите число: '))

try:
	if b == 0:
		raise MyDivisionByZero('Вы не можете делить на 0!')
	else:
		print(a / b)
# except MyDivisionByZero as m:
# 	print(m)
except MyDivisionByZero as m:
	print(m.message)
