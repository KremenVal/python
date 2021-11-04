text_user = None

with open('task-1.txt', 'w') as file:
	while text_user != '':
		text_user = input('Введите текст - ')

		if text_user != '':
			file.write(text_user + '\n')
