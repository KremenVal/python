with open('task-2.txt', 'r', encoding='utf8') as file:
	[print(f"{num + 1}. {line.strip()}\nКоличество слов в строке - {len(line.split())}.") for num, line in enumerate(file)]
