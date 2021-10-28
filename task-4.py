from checks import is_num, is_int, is_float


# Первый вариант через оператор **
def my_func(x, y):
    return x**y


# Воторой вариант через оператор while
# def my_func(x, y):
#     result = 1
#
#     while y < 0:
#         result *= x
#         y += 1
#
#     return 1 / result


nums = {'x': 0, 'y': 0}

for key, value in nums.items():
    while True:
        num = input(f'Введите число {key} - ')

        if is_num(num) and key == 'x':
            if is_int(num) and int(num) > 0:
                nums[key] = int(num)
                break
            elif is_float(num) and float(num) >= 0:
                nums[key] = float(num)
                break
        elif is_int(num) and int(num) <= 0 and key == 'y':
            nums[key] = int(num)
            break

print(my_func(nums['x'], nums['y']))
