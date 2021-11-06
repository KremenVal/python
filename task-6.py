with open('task-6.txt', 'r', encoding='utf-8') as file:
    my_dict = {f"{line.split(':')[0]}": line.split(':')[1].replace('—', '').replace('-', '') for line in file}
    result = {f"{key}": sum(map(lambda el: int(el), [item[0:item.find('(')] for item in value.strip().split()]))
              for key, value in my_dict.items()}

print(result)
