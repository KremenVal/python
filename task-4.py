num, result, div_num = abs(int(input('Please, enter a number - '))), 0, 0

while num > 1:
    div_num = num % 10
    num //= 10

    if div_num > result:
        result = div_num

print(result)
