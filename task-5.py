my_list = [i for i in range(100, -5, -5)]
print("Старый список рейтига - {}".format(my_list))
rating, right_list, final_list = input('Введите натуральное число для рейтинга - '), [], []

if not rating.isdecimal():
    print('Вы ввели не нартуральное число')
else:
    rating = int(rating)

    if rating > max(my_list):
        my_list.insert(0, rating)
    elif rating < min(my_list):
        my_list.insert(len(my_list), rating)
    elif my_list.count(rating) > 0:
        my_list.insert(my_list.index(rating) + my_list.count(rating), rating)
    else:
        while True:
            list_1 = my_list[0:len(my_list) // 2]
            list_2 = my_list[len(my_list) // 2:]

            if list_1[-1] > rating > list_2[0]:
                list_2.insert(0, rating)
                final_list += list_1 + list_2 + right_list
                break
            else:
                if list_1[0] >= rating >= list_1[-1]:
                    if len(list_1) == 2:
                        list_1.insert(1, rating)
                        final_list += list_1 + list_2 + right_list
                        break
                    my_list = list_1
                    right_list = list_2 + right_list
                else:
                    final_list += list_1
                    my_list = list_2
        my_list = final_list

    print("Обновлённый список рейтига - {}".format(my_list))

# Либо испольщовать сортировку как второй вариан решения, в первом я попытался свой алгоритм сделать
# my_list = [i for i in range(100, -5, -5)]
# my_list.append(int(input('Введите число для рейтинга - ')))
# print("Обновлённый список рейтига - {}".format(my_list.sort(reverse=True)))

