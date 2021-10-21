first_day_result = float(input('Введите кол-во км, которое пробежал спортсмен в 1-й день - '))
last_day_result = float(input('Введите кол-во км, которое пробежал спортсмен в последний день - '))

if first_day_result < 0:
    print('Количество км, которое пробежал спортсмен в 1-й день не может быть отрецательным.')
elif last_day_result < 0:
    print('Количество км, которое пробежал спортсмен в последний день не может быть отрецательным.')
else:
    number_of_day = 1

    while first_day_result < last_day_result:
        first_day_result += round(first_day_result * 0.1, 2)
        number_of_day += 1

    print("На {}-й день спортсмен достиг результата - не менее {} км.".format(number_of_day, last_day_result))
