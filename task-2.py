user_time = int(input('Введите любое число в секундах (например, 360) - '))

if user_time < 0:
    print('Время не может быть негативным.')
else:
    hours = str(user_time // 3600)
    minutes = str((user_time - int(hours) * 3600) // 60)
    seconds = str(user_time - (int(hours) * 3600) - (int(minutes) * 60))
    print("{}:{}:{}".format(hours if len(hours) > 1 else '0' + hours, minutes if len(minutes) > 1 else '0' + minutes,
                            seconds if len(seconds) > 1 else '0' + seconds))
