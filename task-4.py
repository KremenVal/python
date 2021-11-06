nums = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

with open('task-4-1.txt', 'r', encoding='utf-8') as file_1:
	with open('task-4-2.txt', 'w', encoding='utf-8') as file_2:
		[file_2.write(line.replace(line.split()[0], nums[line.split()[0].lower()])) for line in file_1]
