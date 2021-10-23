month = input('Введите месяц в виде целого числа от 1 до 12 - ')
season = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

if not month.isdecimal() or int(month) < 1 or int(month) > 12:
    print('Вы ввели неправильный месяц!')
else:
    month = int(month)

    for key, value in season.items():
        if month in value:
            print("Ваш месяц {} относиться к {}".format(month, key))
            break
