# Задание 1
from math import pi

r = 2
a1 = lambda r: pi * (r ** 2)
print('Площадь окружности радиуса', r, ':', (lambda r: pi * (r ** 2))(r))
a = 10
b = 13
print('Площадь прямоугольника размером', a, '*', b, ':', (lambda a, b: a * b)(a, b))
a1 = 7
b1 = 5
h = 3
print('Площадь трапеции для а=', a1, ',b=', b1, ',h=', h, ':', (lambda a, b, h: (a + b) * h / 2)(a1, b1, h))

# Задание 2
print()
print('Произведение трех чисел 2,5,5 =', (lambda i, j, k: i * j * k)(2, 5, 5))

# Задание 3

lst = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98},
]
res = sorted(lst, key=lambda score: score['name'])
print('Список с сортировкой по имени:')
print(res)
res1 = sorted(lst, key=lambda score: score["final"], reverse=True)
print('Список с сортировкой по оценке по убыванию:')
print(res1)

res2 = min(lst, key=lambda score: score["final"])
print('MIN:', res2)
res3 = max(lst, key=lambda score: score["final"])
print('MAX:', res3)

# Задание 4

lst2 = [3, 6, 8, 9, 1, 2]
print('Изнач. список:', lst2)
fin_res = (list(map(lambda t: t * lst2.index(t) ** 3, lst2)))
print('Произведение элемента на порядковый номер в кубе:', fin_res)

# Задание 5

nums = [3, 5, 7, 3, 9, 5, 7, 2]
print('Изнач. список:', nums)
print('Все значение в квадрате:', (list(map(lambda i: i ** 2, nums))))
print('Все значение в кубе:', (list(map(lambda i: i ** 3, nums))))
