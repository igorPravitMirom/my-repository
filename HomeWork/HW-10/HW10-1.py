# Task 1
print('Задание 1')
a = ['red', 'green', 'blue']
b = ['#FF000', '#008000', '#0000FF']
d = dict(zip(a, b))
print(d)

# Task 2
print('Задание 2')
d2 = {i: i ** 3 for i in range(1, 11)}
print(d2)

# Task 3
print('Задание 3')
lst1 = ['color', 'fruit', 'pet']
lst2 = ['blue', 'apple', 'dog']
d3 = {lst1[i]: lst2[i] for i in range(len(lst1))}
print(d3)

# Task 4
print('Задание 4')


def min_func(*args):
    print('Минимальное число: ', min(user_list))


print('Поочередно вводите числа(Чтобы закончить введите 0 ("нуль"))')
user_list = []
while True:
    user_input = int(input("->"))
    if user_input != 0:
        user_list.append(user_input)
    else:
        break
print('Вы ввели:', user_list)
min_func(user_list)

# Task 5
print('Задание 5')


def sum_func(*args):
    new_list = []
    for i in args[0]:
        if len(new_list) == 0:
            new_list.append(i)
        else:
            new_list.append(new_list[-1] + i)
    print('Результат:', new_list)


print('Поочередно вводите числа(Чтобы закончить введите 0 ("нуль"))')
user_list2 = []
while True:
    user_input2 = int(input("->"))
    if user_input2 != 0:
        user_list2.append(user_input2)
    else:
        break
print('Вы ввели:', user_list2)
sum_func(user_list2)
