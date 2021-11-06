from time import sleep


class TrafficLight:
	__color = ['красный', 'жёлтый', 'зелёный']

	def running(self):
		my_dict = {'красный': 7, 'жёлтый': 2, 'зелёный': 5}
		keys = list(my_dict.keys())

		if self.__color[0] != keys[0] or self.__color[1] != keys[1] or self.__color[2] != keys[2]:
			print('Неправильный порядок режимов.')
		else:
			while True:
				for item in self.__color:
					print(item)
					sleep(my_dict[item])


trafficLight = TrafficLight()
trafficLight.running()
