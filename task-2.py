import random

my_list = [random.randrange(0, 1000) for _ in range(0, 10)]
print([my_list[i + 1] for i in range(0, len(my_list) - 1) if my_list[i + 1] > my_list[i]])
