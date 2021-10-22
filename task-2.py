my_list = input('Введите любую последовательность из чисел или текста через запятую (,), пример (1,2,b) - ').split(',')
len_my_list = len(my_list)
len_my_list -= 1 if len_my_list % 2 != 0 else 0

for i in range(0, len_my_list, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
