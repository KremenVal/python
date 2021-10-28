from checks import is_num, is_int


def my_div(a, b):
    return a / b if b != 0 else print('Деление на 0!')


nums = {1: 0, 2: 0}

for key, value in nums.items():
    while True:
        num = input(f'Введите число {key} - ')

        if is_num(num):
            nums[key] = int(num) if is_int(num) else float(num)
            break

print(my_div(nums[1], nums[2]))
