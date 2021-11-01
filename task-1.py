from checks import is_num, is_int


def salary(output_in_hours=10, rate_per_hour=100, bonus=0):
	return (output_in_hours * rate_per_hour) + bonus


my_dict = {'выработку': 0, 'ставку': 0, 'премия': 0}

for key, value in my_dict.items():
	while True:
		num = input(f'Введите {key} - ')

		if is_num(num):
			my_dict[key] = int(num) if is_int(num) else float(num)
			break
		elif key == 'премия' and num == '':
			break

print(salary(my_dict['выработку'], my_dict['ставку'], my_dict['премия']))
