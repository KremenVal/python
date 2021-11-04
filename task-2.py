count_lines = 1

with open('task-2.txt', 'r', encoding='utf8') as file:
	while True:
		line = file.readline()

		if not line:
			break

		print("{}. {}\nКоличество слов в строке - {}.".format(count_lines, line.strip('\n'), len(line.split())))
		count_lines += 1
