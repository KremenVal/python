proceeds, costs = int(input('Введите выручку фирмы - ')), int(input('Введите издержки фирмы - '))
income = proceeds - costs

print("Финансовый результат фирмы - {}.".format('прибыль' if income > 0 else 'убыток'))

if income > 0:
    profitability_of_proceeds = (income / proceeds) * 100

    print("Рентабельность выручки - {}%.".format(profitability_of_proceeds))

    number_of_employees = int(input('Введите численность сотрудников фирмы - '))

    if number_of_employees < 1:
        print('На фирме не может работать 0 или меньше сотрудников.')
    else:
        profit_per_employees = income / number_of_employees

        print("Прибыль фирмы в расчёте на одного сотрудника - {}.".format(profit_per_employees))
