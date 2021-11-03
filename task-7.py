from random import randrange


def fact(number):
	result = 1

	if number == 1:
		yield "{}! = {}".format(number, number)
	else:
		for i in range(1, number + 1):
			result *= i

			yield "{}! = {}".format(i, result)


num = randrange(0, 50)

for el in fact(num):
	print(el)
