from math import sqrt, pi

print('Вычисление площади фигур\nВыбор фигуры: \n1 - треугольник\n2 - прямоугольник \n'
      '3 - круг')

choose = int(input('Введите номер фигуры: '))
if choose == 1:
    a = int(input('Введите сторону a: '))
    b = int(input('Введите сторону b: '))
    c = int(input('Введите сторону c: '))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь треугольника: ', s)
elif choose == 2:
    a = int(input('Введите сторону a: '))
    b = int(input('Введите сторону b: '))
    s = a * b
    print('Площадь прямоугольника: ', s)
elif choose == 3:
    r = int(input('Введите радиус окружности r: '))
    s = pi * r**2
    print('Площадь окружности: ', s)
else:
    print('К сожалению программа вычисляет только эти три фигуры')
print('До свидания!')
