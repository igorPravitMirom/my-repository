d = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500},
}


def worker_list():
    count = 1
    for key in d:
        print(count, ')', d[key]['name'], ' ,зарплата:', d[key]['salary'])
        count += 1


worker_list()
person = int(input('Введите номер работника, которому хотите изменить зарплату: '))
new_salary = int(input('Введите новую зарплату сотрудника: '))
if person == 1:
    d['emp1']['salary'] = new_salary
elif person == 2:
    d['emp2']['salary'] = new_salary
elif person == 3:
    d['emp3']['salary'] = new_salary
else:
    print('Такого работника не найдено!')
worker_list()