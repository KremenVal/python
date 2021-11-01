from checks import is_num, is_int

my_dict = {'выработку': 0, 'ставку': 0, 'премия': 0}

for key, value in my_dict.items():
	while True:
		num = input(f'Введите {key} - ')

		if is_num(num):
			my_dict[key] = int(num) if is_int(num) else float(num)
			break
