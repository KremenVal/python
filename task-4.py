words = input('Введите строку из нескольких слов, разделённых пробелами - ').split(' ')

if words[0]:
    for i in range(len(words)):
        print("{}. {}".format(i + 1, words[i] if len(words[i]) < 11 else words[i][:10]))
