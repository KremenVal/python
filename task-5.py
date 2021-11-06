from random import randrange


with open('task-5.txt', 'w+') as file:
	file.write(' '.join([str(randrange(0, 1000)) for _ in range(0, 1000)]))
	file.seek(0)
	print(sum(map(lambda element: int(element), file.readline().split())))
