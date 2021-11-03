from itertools import count, cycle
from random import randrange


num_start = randrange(0, 100)
num_end = randrange(100, 150)

for i in count(num_start):
	print(i)

	if num_end == i:
		break

my_list = [randrange(0, 100) for _ in range(0, 10)]
iter_list = cycle(my_list)
end_cycle = randrange(10, 50)

while end_cycle > 0:
	print(next(iter_list))
	end_cycle -= 1
