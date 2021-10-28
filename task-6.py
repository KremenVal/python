def int_func(string: str) -> str:
    return string.title()


while True:
    string_input = input('Введите латинские буквы/слова - ')

    if not string_input.isascii() or not string_input.isalpha() or not string_input.islower():
        print('Не верные данные')
    else:
        print(int_func(string_input))
        break
