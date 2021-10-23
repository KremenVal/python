rating, my_list = int(input('Введите число для рейтинга - ')), [7, 5, 3, 3, 2]
list_1 = my_list[0:len(my_list) // 2]
list_2 = my_list[len(my_list) // 2:]

if rating > max(my_list):
    my_list.insert(0, rating)
elif rating < min(my_list):
    my_list.insert(len(my_list), rating)
else:
    list_range_1 = [i for i in range(list_1[0], list_1[-1] - 1, -1)]
    list_range_2 = [i for i in range(list_2[0], list_2[-1] - 1, -1)]

    if rating not in list_range_1 and rating not in list_range_2:
        list_2.insert(0, rating)
    else:
        if rating in list_range_1:
            link_list = list_1
        else:
            link_list = list_2
        for j in range(0, len(link_list) - 1):
            if link_list[j] >= rating >= link_list[j + 1]:
                link_list.insert(j + 1, rating)
                break

    my_list = list_1 + list_2

print(my_list)
