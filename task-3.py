class NotNumber(Exception):
	def __init__(self, *args):
		if args:
			self.message = args[0]
		else:
			self.message = None

	def __str__(self):
		if self.message:
			return self.message
		else:
			return 'Not a Number'


def list_int():
	result_list = []

	while True:
		item = input('Введите число или слово "stop" для остановки скрипта: ')

		try:
			if not item.isdecimal():
				if item.lower() == 'stop':
					break
				else:
					raise NotNumber('Вы ввели не число')
			else:
				result_list.append(int(item))
		except NotNumber as nn:
			print(nn)

	return result_list


print(list_int())
