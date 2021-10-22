my_list = [
    1, 'string', [1, 'string', tuple('Hello World!'), set('Hello World!'), {'1': 1, '2': 2}, True, bytes(27), None],
    tuple('Hello World!'), set('Hello World!'), {'1': 1, '2': 2}, True, bytes(27), None
]

for i in my_list:
    print(type(i))
