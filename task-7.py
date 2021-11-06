import json


with open('task-7.txt', 'r', encoding='utf-8') as file:
    firms = {f"{line.split()[0]}": float(line.split()[2]) - float(line.split()[3]) for line in file}
    average = {'average_profit': sum([profit for firm, profit in firms.items() if profit > 0]) /
               len([profit for firm, profit in firms.items() if profit > 0])}

with open('task-7.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps([firms, average]))
