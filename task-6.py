data, number, analytics = [], 1, {'название': [], 'цена': [], 'количество': [], 'ед': []}

while True:
    data.append((number, {
        'название': input('Введите название продукта - '),
        'цена': int(input('Введите цену продукта - ')),
        'количество': int(input('Введите количество продукта - ')),
        'ед': input('Введите название единиц - '),
    }))

    number += 1
    flag = input('Если хотите продолжить ввод, введите 1, если нет - 2: ')

    if flag == '2':
        break

for key, value in analytics.items():
    for i in range(0, len(data)):
        for data_key, data_value in data[i][1].items():
            if key == data_key:
                value.append(data_value)

if len(analytics['ед']) == analytics['ед'].count(analytics['ед'][0]):
    analytics['ед'] = [analytics['ед'][0]]
print(analytics)
