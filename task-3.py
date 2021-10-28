def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    my_list.remove(min(my_list))

    return sum(my_list)


print(my_func(1, -12.5, 100))
