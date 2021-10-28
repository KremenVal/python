from checks import is_num, is_int


result = 0

while True:
    nums = input('Строку чисел, разделенных пробелом или стоп символ s для окончания работы программы - ')

    if nums.lower() == 's':
        break
    else:
        nums = nums.split(' ')

        for i in nums:
            if is_num(i):
                result += int(i) if is_int(i) else float(i)

        print(result)

print(result)
