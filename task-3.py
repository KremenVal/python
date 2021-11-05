employees, sum_of_salary = {}, 0

with open('task-3.txt', 'r', encoding='utf-8') as file:
	for line in file:
		key, value = line.split()

		if key in employees:
			employees[key].append(float(value))
		else:
			employees[key] = [float(value)]

for employee, salaries in employees.items():
	[print(f"Сотрудник {employee} имеет оклад {salary}.") for salary in salaries if salary < 20000]
	sum_of_salary += sum(salaries)

print(f"Средняя величина дохода сотрудников - {sum_of_salary / len(employees)}")
