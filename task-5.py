class Stationery:
	title = ''

	def draw(self):
		print('Запуск отрисовки.')


class Pen(Stationery):
	def draw(self):
		Stationery.draw(self)
		print('Ручку нельзя стереть.')


class Pencil(Stationery):
	def draw(self):
		Stationery.draw(self)
		print('Карандаш можно стереть.')


class Handle(Stationery):
	def draw(self):
		Stationery.draw(self)
		print('И эту ручку нельзя стереть.')


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
