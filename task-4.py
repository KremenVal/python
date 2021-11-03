from random import randrange

my_list = [randrange(0, 1000) for _ in range(0, 10)]
print([i for i in my_list if my_list.count(i) == 1])
