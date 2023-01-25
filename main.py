# name = "Igor"
# surname_my = "Osokin"
# print("Hello", name, surname_my)
# age = 20
# print(age)
# print(id(age))
# print(type(age))
# a = 1
# b = 2
# c = a
# b = c
# a = a+b
# b = a - b
# a = a-b
# a, b = b, a
# print("a =",a)
# print("b=",b)

# print("строка символов")
# print('строка \n символов ')
# print('\tДокумент   "file.txt" D:\\folder\\file.py')

# s1 = 'Hello'
# s2 = "Python"
# s3 = s1 + " " + s2 +"!\t\t"
# print(s3)
# print(s3*3)
# print("Выполнил задание \"\" ")

# password = "qwe"
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print("Пользователь")
#     case 'moderator':
#         print('Модератор')
#     case _: #Для всех остальных случаев, подчеркивание аналог default
#         print("Пароль не верен")

# Аналог switch'а из JS
# day = "понедельник"
# time = 17
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:  # Символ "|" - аналог "или" , поволяет перечислять несколько значений
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:  # Для всех остальных случаев, подчеркивание аналог default
#         print("Такого дня не существует или не рабочее время")

# Тернарный оператор
# a, b = 10, 20
#
# minim = a if a<b else b
# print(minim)

# a, b = 140, 20
# print("a==b" if a == b else "a>b" if a > b else "b>a")
# #Можно создавать вложенность и несколько вариаций

# num=int(input("Введите число"))
# delit=int(input("Введите делитель"))
# print(num/delit if delit!=0 else "Делить нельзя")

# Исключения

# 2a=0 - SyntaxError

# a = 0
# print(a+b) -NameError: name 'b' is not defined

# try:
#     n = int(input("Введите целое число")) #Если введут не целое число, выдаст ошибку
#     print(n*2)
# except ValueError: #ставим тип ошибки
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель"))
#     print(n/m)
# except ValueError: #ставим тип ошибки
#     print("Что-то пошло не так")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# Добавили на случай еще для одной ошибки

# try: #ПОПЫТАЙСЯ
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель"))
#     print(n/m)
# except (ValueError, ZeroDivisionError): #Скобки обязательны
#     print("Нельзя вводить строки и делить на ноль")
# else: #если не зашли в except
#     print("Все нормально. Вы ввели числа",n,"и",m)
# finally: #Отработает всегда в любом случае
#     print("Конец программы")

# try:
#     first = (input("Введите первое значение: "))
#     second = (input("Введите второе значение"))
#     print(int(first)+int(second))
# except ValueError:
#     print(str(first)+str(second))

# Циклы

# While
# i = 2
# while i <= 20:
#     if i%2 == 0:
#         print("i=",i, end=" ")
#     i += 1

# num = int(input("Введите число: "))
# i = 0
# string = ""
# while i < num:
#     string += "*"
#     i+=1
# print(string)

# start = int(input("Начало"))
# # end = int(input("Конец"))
# # summa=0
# # while start < end:
# #     if start % 2 != 0:
# #         summa += start
# #         print(start,'+',end="")
# #     start +=1
# # print('=',summa)

# n = input("Введите целое число")
# while type (n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое или строка")
#         n = input("Введите целое число")
# if n % 2 == 0:
#    print('Число четное')
# else:
#     print('Число нечетное')

# i=0
# # while i<10:
# #     if i == 3:
# #         i+=1
# #         continue #Пропустит i=3 и начнет цикл дальше
# #     print("i=",i,end=' ')
# #     if i==5:
# #         break #Прерывает цикл
# #     i+=1
# # print("Цикл завершен")

# i=0
# while True:
#     print(i)
#     if i ==5:
#         break #Прервет цикл на 5
#     i+=1

# while True:
#     n= int(input("Введите положительное число: "))
#     if n < 0:
#         break

# end=1
# while True:
#     n = int(input("Введите число: "))
#     if n==0:
#         break
#     end *= n
# print("Произведение равно: ",end)

# i = 0
# while i < 10:
#     if i ==5:
#         break
#     print(i)
#     i+=1
# else: #не отработает ,если не отработает while до конца или прервется
#     print('Цикл окончен, i=',i)

# Вложенный цикл
# i = 1
# while i < 5:
#     print('Внешний цикл: i=',i)
#     j=1
#     while j < 4:
#         print("\tВнутренний цикл: j=",j)
#         j+=1
#     i+=1

# i = 1
# while i < 10:
#     j = 1
#     while j<10:
#         print(i, '*', j,'=',i*j, '\t\t',end='')
#         j += 1
#     print()
#     i += 1

# for element in collection:
#   тело цикла

# for i in "Hello",'red','blue',20,0.5:
#     print(i)

# print(range(5))

# range(start, stop(finish), step)
# Минимум одно значение - оно и будет stop, отсчет будет начинаться с Нуля
# Можно пойти в обратную сторону: for i in range(100,5,-2):
# В рендж могут быть только целые числа
# for i in range(5,100,2):
#     print(i,end=' ')

# Аналогичный цикл через while
# i = 5
# while i < 100:
#     print(i,end=' ')
#     i+=5

# num = int(input("Введите целое число: "))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i,end=' ')

# for i in range(10,100):
#     if i%10 == i //10:
#         print(i,end=' ')

# for i in range(3):
#     print(i,end=' ')
#     if i == 1:
#         break #Если цикл прервется здесь, то else не сработает
# else:
#     print('\n done')

# for i in range(3):
#     print('+++',i)
#     for j in range(2):
#         print('----',j)

# w = int(input('W = '))
# h = int(input('H = '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# letter =[i for i in 'Hello']
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)

# nums = [5,45,4,5,23,23,4,5]
# print(nums)
# print(type(nums)) #<class 'list'>
# print(nums[0]) #5
# print(nums[-3]) #23
# nums[-2] = 2 # перезапишет предпоследний элемент
# print(nums)
# print('элементов:', len(nums))

# s = []
# print(s)
# b = list()  # Функция явного приведение данных
# print(b)
# c = list('Hello')
# print(c)

# В список добавили 6 элементов (внутри списка)
# s = [5] * 6
# print(s)  # [5, 5, 5, 5, 5, 5]
#
# #Списки можно складывать
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a+b
# print(c) #[1, 2, 3, 4, 5, 6]

# Генерация массива на основе ренджа
# n=list(range(10))
# print(n) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [выражение for переменная in последовательность]

# n = 5
# a = [i**2 for i in range(n)]
# print(a) #[0, 1, 4, 9, 16]

# n = 5
# a = [i*2 for i in 'Hello']
# print(a) #['HH', 'ee', 'll', 'll', 'oo']

# a = [0] * int(input('Ввести количество элементов списка: '))
# print(a)
# for i in range(len(a)): #Длиниа списка 'a'
#     a[i] = int(input('-->')) #Заполняем список элементами a-количество раз
# print(a)

# Короткая версия
# a = [int(input('-->')) for i in range(int(input('Ввести количество элементов списка: ')))]
# print(a)

# nums = [5,45,4,5,23,23,4,5]
# print(nums*2)
# for i in range(len(nums)):
#     print(nums[i],end=' ') #5 45 4 5 23 23 4 5
# print()
# for i in nums:
#     print(i*2,end=' ') #5 45 4 5 23 23 4 5

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# summa=0
# for i in a:
#     if i<0:
#         summa+=i
# print(summa)

# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += i
# print('Четных: ', odd, 'Нечетных: ', even)

# a = [int(input('-->')) for i in range(int(input('n: ')))]
# zero=0
# summa=0
# for i in a:
#     if i==0:
#         zero+=1
#     else:
#         summa+=i
# print('Результат: ', (summa/(len(a)-zero)))

# a = [int(input('-->')) for i in range(int(input('n= ')))]
# print(a)
# for i in range(1,len(a)):
#     if a[i]>a[i-1]:
#         print(a[i],end=' ')

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# Срезы
# список[start:stop:step]

# a = [9, 1, 3, 53, 5, 17]
# print(a[1:4]) #[1, 3, 4] Взяли диапазон от индекса "1" до "4" , "4" индекс не включает
# print((a[1:])) #от индекса 1 до конца списка [1, 3, 53, 5, 17]
# print(a[:]) #все
# print(a[-1:1:-1]) #[17, 5, 53, 3]
# print(a[::-1]) #[17, 5, 53, 3, 1, 9]
#
# a = list(range(1,8))
# print(a)
# print(a[::-1])

# a = list(range(1, 8))
# print(a)
# a[1:3] = [0,0,0,0]
# print(a)
# # a[1:2] = [20] # Вместо значений в списке с 1 индексом заменится значением 20
# # print(a)
# # a[2] = [50] # добавляется вложенный список
# # print(a)
# a[3:5] = []
# print(a)
# del a[0] # удалит первый элемент
# print(a)
# del a[0:3] #удалить элементы с 1 по 3(по индексу)
# print(a)
# del a[:] #Удалить все элементы
# print(a)n

# Методы списков

# print(dir(list)) #функция dir(что интересует) показывает все функции

# a = list(range(1, 8))
# print(a) #[1, 2, 3, 4, 5, 6, 7]
#
# # a.append(99) #Добавляет элемент в конец списка(ТОЛЬКО ОДИН ЭЛЕМЕНТ!)
# # print(a) #[1, 2, 3, 4, 5, 6, 7, 99]
#
# # a.extend([22,11,3]) #ПОзволяет добавлять множество элементов в конец списка
# # print(a) #[1, 2, 3, 4, 5, 6, 7, 22, 11, 3]
# a.extend('add') #[1, 2, 3, 4, 5, 6, 7, 'a', 'd', 'd']
# print(a)

# a.insert(0, 100) #Добавляет по индексу элемент, 0-индекс,100-элемент
# print(a)

# n = int(input('Введите кол-во элементов списка: '))
# s = []
# for num in range(n):
#     x = input('-->')
#     s.append(x)
# print(s)

# n = int(input('Введите кол-во элементов списка: '))
# s = []
# for num in range(n):
#     x = int(input('-->'))
#     if x %3 == 0:
#         s.append(x)
#     else:
#         print('Число',x,'не делится на 3 без остатка.')
# print(s)

# a = [5, 9, 2, 1, 4, 3,2,4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c: #Проверяет есть ли а в новом списке "с"
#             continue
#         if i==j:
#             c.append(i)
# print(c) #[2, 1, 4, 3]

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# n = 0
# while n < len(a):
#     c.append(a[n])
#     c.append(b[n])
#     n += 1
# print(c)

# Методы удаления
# b = [11, 22, 33, 2, 3, 22]
# b.remove(22) #Удалится первое значение,которое встретится
# print(b) #[11, 33, 2, 3, 22]
# b.remove(0) #Выдаст ошибку, т.к. элемента нет
# a=0
# if a in b:
#     b.remove(a)
# print(b)

# a = b.pop() #с пустыми скобками - удаляет последний элемент списка
# print(b) #[11, 22, 33, 2, 3]
# print(a) #22

# a = b.pop(2) #удалит элемент по индексу "2"
# print(b) #[11, 22, 2, 3, 22]
# print(a) #33

# b.clear() #Очищает весь список
# print(b) #[]

# b = [11, 22, 33, 2, 3, 22, 2, 3, 2]
# # num=b.count(2) #Количество заданых значений в списке
# # print(num)
#
# # ind = b.index(2) #Первое значение ,выведет индекс в списке
# # print(ind)
# ind = b.index(2,2,-1) #3
# print(ind)

# a = [11, 22, 33, 2, 3, 22, 2, 3, 2]
# b=a
# # print("a",a)
# # print("b",b)
# # a.append(20) #"20" внесется в оба списка в конец
# # print("a",a)
# # print("b",b)
# # a = [11, 22, 33, 2, 3, 22, 2, 3, 2]
# b=a.copy() # "b" берет копию с "а"
# a.append(20) #"20" внесется только в список "а"
# print("a",a)
# print("b",b)

# a = [11, 22, 33, 2, 3, 22, 2, 3, 2]
# a.reverse() #перестраивает список задом наперед
# print(a) #[2, 3, 2, 22, 3, 2, 33, 22, 11]

# a = [11, 22, 33, 2, 3, 22, 2, 3, 2]
# a.sort() #[2, 2, 2, 3, 3, 11, 22, 22, 33] по умолчанию-по возрастанию
# print(a)

# import random as r
#
# print(r.randint(2, 9))
# print(r.randrange(1, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 3))
#
# city = ['Москва',"Новосибирск","Воронеж","Сочи","Екатеренбург"]
# print(r.choice(city)) #Выбирает один из городов случайно
# print(r.choices(city, k=3)) #Выбирает 3 города из списка(могут повторятся)
#
# r.shuffle(city) #Перемешивает список
# print(city)

import random as r

# mas = [i for i in range(10)]
# print(mas) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# mas = [r.randint(0,100) for i in range(10)]
# print(mas) #[83, 88, 60, 22, 28, 62, 42, 80, 91, 60] будут случайные числа

# lst = [5, 4, 3, 2, 1]
# lst = ['a','b','c','d','e','f']
# print(len(lst)) #5 -количество
# print(max(lst)) #5 -максимальное число
# print(min(lst)) #1 -минимальное
# print(sum(lst)) #15 - сумма элементов(


# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
# print(res)

# x = list('21k3h2hj')
# print(x)
# print('k' in x) #Находится ли "к" в списке "х"? вывод: TRUE
# print('k' not in x) #false

# from random import randint
#
# n1 = int(input('Введите размер первого списка'))
# n2 = int(input('Введите размер второго списка'))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('Первый список: ', a)
# print('Второй список: ', b)
# c = a + b
# print('Третий список: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Элементы обоих списков без повторений:', c)


# from random import randint
#
# n1 = int(input('Введите размер первого списка'))
# n2 = int(input('Введите размер второго списка'))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# c = []
# print('Первый список: ', a)
# print('Второй список: ', b)
# for i in range(len(a)):
#     if a[i] in b:
#         if a[i] not in c:
#             c.append(a[i])
# print(c)

# from random import randint
#
# a = []
# step = 0
# n1 = int(input('Введите размер первого списка'))
# while step < n1:
#     i = randint(0, n1)
#     if i not in a:
#         a.append(i)
#     else:
#         step-=1
#     step +=1
# print(a)

# m = [
#     [1, 2, 3, 4, 9, 5],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col],end='\t')
#     print()

# Вариант второй
# for row in m:
#     for x in row:
#         print(x,end='\t')
#     print()
#
# w, h = 5, 3
# # matrix = [[0 for x in range(w)] for y in range(h)]
# #ОБЬЯСНЕНИЕ СТРОКИ ВЫШЕ:
# matrix=[]
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(x*y)
#     matrix.append(new_row)

# for row in matrix:
#     for x in row:
#         print(x,end='\t')
#     print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# from random import randint
# w, h = 3, 4
# n=0
# matrix = [[randint(-20,10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x<0:
#             n+=1
#         print(x,end='\t\t')
#     print()
# print('n=',n)

# from random import randint
#
# w, h = 3, 4
# n = 1
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x != 0:
#             n *= x
#         print(x, end='\t\t')
#     print()
# print('n=', n)


# import math

# num1 = math.sqrt(2)
# num2 = math.ceil(3.2)  # Округление в большую сторону
# num3 = math.floor(3.8)  # округление в мельшую сторону
# print(num1)
# print(num2)
# print(num3)

# import math as m
# from math import sqrt, ceil, floor,pi

# num1 = sqrt(2)
# num2 = ceil(3.2)  # Округление в большую сторону
# num3 = floor(3.8)  # округление в мельшую сторону
# print(num1)
# print(num2)
# print(num3)
# print(pi)

# from math import sqrt, ceil, floor, pi
#
# num = int(input('Введите радиус окружности: '))
# print('Длина окружности: ', round(2 * pi * num, 2))


import time
import locale

# seconds = time.time()
# print(seconds) #1672070712.5709333 Время в секундах с 1970года
#
# local_time = time.ctime()
# local_time = time.ctime(432432432) #Thu Sep 15 02:07:12 1983.Передали в секундах время
# print(local_time) #Mon Dec 26 18:05:12 2022

# res = time.localtime()
# print(res) #time.struct_time(tm_year=2022, tm_mon=12, tm_mday=26, tm_hour=18, tm_min=8, tm_sec=13, tm_wday=0, tm_yday=360, tm_isdst=0)
# print(res.tm_year) #2022

# print(time.strftime("Today is %B, %Y")) #Today is December, 2022
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))  #26/12/2022, 18:17:38
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(34243234))) #01/02/1971, 10:00:34
# print(time.strftime("Сегодня: %B, %Y")) #Сегодня: December, 2022
#
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime("Сегодня: %B, %Y")) #Сегодня: Декабрь, 2022

# Ставим таймер на выполнение команды
# pause = 5
# print("Programm started...")
# time.sleep(pause)
# print(pause, 'seconds')

# text = input('Название напоминания: ')
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time) #Остановит выполнение когда на заданное число
# print(text)

# start = time.time()
# time.sleep(5) #Тут может быть любой код
# finish= time.time()
# res = finish - start
# print(res, 'Sec.') #5.0009472370147705 Sec.
#
#
# start = time.monotonic()
# time.sleep(5) #Тут может быть любой код
# finish= time.monotonic()
# res = finish - start
# print(res, 'Sec.') #5.0 Sec.

# Функции
# a = 2
#
#
# def hello(name):  # создали функцию
#     print('Hello',name)  # по синтаксису желательно 2 строки сверху и снизу
#
#
# hello('Igor') #Если применяемый аргумент есть, обязательно передать его при вызове
# # hello()  # вызвали функцию


# def hello(name, word):  # создали функцию
#     print('Hello ', name, ' ,Say: ', word, sep="")  # по синтаксису желательно 2 строки сверху и снизу
#
#
# hello('Igor', 'my phrase')  # Передали два параметра

# def get_sum(a, b):
#     x = 1
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', '123')


# def symbol(count, a, b):
#     # print((a + b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#
#     # Напишем for в одну строку:
#     print([a if i % 2 == 0 else b for i in range(count)])  # ['+', '-', '+', '-', '+', '-', '+', '-', '+']
#
#
# symbol(9, '+', '-')

# def get_sum(a, b):
#     return a + b # команда return возвращает значения из тела функции
#
#
# x = 2
# y = 5
# w = get_sum(x, y)  # Вернулось значение 7 из функции
# print(w)


# def get_sum(a, b):
#     print(a + b)
#     return #Прервет цикл
#
#
# x = 2
# y = 5


# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(5, 3):
#     print('Первое число больше')
# else:
#     print('Второе число больше')


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for i in password:
#         if "A" <= i <= "Z":
#             has_upper = True
#         if 'a' <= i <= 'z':
#             has_lower = True
#         if '0' <= i <= '9':
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Пароль надежный')
# else:
#     print('Пароль не надежный')


# def cube(num):
#     return num ** 3
#
#
# for i in range(1, 11):
#     print(i, 'в кубе = ', cube(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop() #Удаляет последний элемент и сохраняет его в 'end'
#     start = lst.pop(0) #Удаляет 1 элемент
#     lst.insert(0, end) #Добавляет в начало
#     lst.append(start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))
# print([3]+[2,4]+[1])

# def get_sum(a, b, c=0, d=0):  # Задали 'd' значение по умолчанию,если его не передали
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 6))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 2))
# print(get_sum(1, 2, d=5)) #Задали чтоб значение d передавалось "5"

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр:')
# print(digits_sum(98347283))
# print(digits_sum(983471))
# print(digits_sum(98347281213))
# print('Сумма нечетных цифр: ')
# print(digits_sum(98347283, even=False))
# print(digits_sum(983471, even=False))
# print(digits_sum(98347281213, even=False))


# def display_info(name, age):
#     print('Name:', name, 'age: ', age)
#
#
# display_info('Igor', 23)
# display_info(age=23, name='Igor')

# Изменяемые и неизменяемые объекты
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)
# print((lst1 is lst2))
# print('id1:', id(lst1))
# print('id2:', id(lst2))
#
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print('a:', id(a))
# print('b:', id(b))

# lst1 = [1, 2, 3]
# print('id1:', id(lst1))  # id: ...568
# lst1.append(4)
# print(lst1)
# print('id1:', id(lst1))  # id: ...568

# a='с'
# b='c'
# print(id(a))
# print(id(b))
#
# lst1 = [1, 2, 3]
# lst2 = lst1
# print(lst1 == lst2)
# print((lst1 is lst2))
# print('id1:', id(lst1))
# print('id2:', id(lst2))

# Кортеж(tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# lst[1] = 50
# print(lst[1])  # 20
# print(lst.__sizeof__())
# #tpl[1] = 50 # Не поддерживает изменения
# print(tpl[1])  # 20
# print(tpl.__sizeof__())

# a = (1,2,3,4,5)
# print(type(a))  # <class 'tuple'>
# b = tuple(a)
# print(type(b))  # <class 'tuple'>
# print(b)
# b = tuple([1,2,3,4,5])
# print(b) #(1, 2, 3, 4, 5)
#
# #КОртеж с 1 элементом
# c = (2,)
# print(type(c)) #<class 'tuple'>
# print(c)

# a = (1, 2, 3, 4, 5)
# b = (1, 2, 3, 4, 5)
# print(id(a))
# print(id(b))  # ID будет одинаковый
#

# t = tuple('hello')
# print(type(t)) #<class 'tuple'>
# print(t) #('h', 'e', 'l', 'l', 'o')
# print(t[1]) #e
# print(t[1:3]) #('e', 'l')

# s = tuple([input('->') for i in range(3)])
# print(s)

# s = input('->')  # 231213
# s = tuple(s)
# print(s)  # ('2', '3', '1', '2', '1', '3')


from random import randint


# s = tuple(randint(1,30) for i in range(3))
# print(s)

# s = tuple(2**(i+1) for i in range(12))
# print(s) #(2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)


# t1 = tuple('Hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)  # ('H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd')
# print(len(t3))  # 10
# print(t3.count('l'))  # Считает количество элементов 'l'
# print(t3.index('l'))  # Находит первый индекс элемента с нужным значением
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print('Такого элемента нет') # сработает это т.к. "а" нету в кортеже
# for i in t3:
#     print(i,end='') #Helloworld


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # first = tpl.index(el)
#             # second = tpl.index(el, first + 1)
#             # return tpl[first:second+1]
#             return tpl[tpl.index(el): tpl.index(el, tpl.index(el) + 1)]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# def tpl_gen(a, b):
#     return tuple(randint(a, b) for _ in range(5))
#
#
# t1 = tpl_gen(0, 5)
# t2 = tpl_gen(-5, 0)
# print(t1)
# print(t2)
# print(t1 + t2, (t1 + t2).count(0))


# point = (0, 20)
# match point:
#     case (x, y):
#         print("Точка находится в координатах ", x, 'по оси Х и по Y:', y)
#     case (0, 0):
#         print('Точка находится в координатах 0:0')
#     case (x, 0):
#         print("Точка находится в координатах ", x, 'по оси Х и по Y:0')
#     case (0, y):
#         print('Точка находится в координатах по оси Х:0 и по Y:', y)
#     case _:
#     case _: # для незнакомых значений
#         print('это не координаты точки')


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t,id(t))
# print(len(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t,id(t))
# print(len(t))

# Распаковка кортежей

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # Присваивает значения из кортежа в переменные
# print(x)  # 1
# print(y)  # 2
# print(z)  # 3


# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # name1, age1, married1 = user
# name1, age1, married1 = get_user()
# print(name1, age1, married1)


# УДалить элемент кортежа не получится!!!
# a = (1, 2)
# # del a[0]  # не получится
# print(a)


# Преобразование кортежей в списки и обратно
# lst = [1,2,3,4,5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)


# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6))),
# )
# print(countries)
# print()
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print('\nСтрана:',countryName, 'население:',countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print('\tГород:', cityName, 'население:', cityPopulation)


# ТИП ДАННЫХ МНОЖЕСТВО
# set()

# s = {'banana', 'apple', 'orange'}
# print(s)  # {'banana', 'apple', 'orange'}
# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)  # {'banana', 'apple', 'orange'}
# print(len(s))  # 3
# # set() - множество с уникальными данными, НЕ УПОРЯДОЧЕН!
#
# # Создание множеств:
# a = {}
# print(type(a))  # <class 'dict'>

# a = set('hello')
# print(type(a))  # <class 'set'>
# print(a)  # {'o', 'h', 'e', 'l'}
#
# c = ['red', 'green', 'yellow', 'blue', 'green']
# b = set(c)
# print(b)  # {'green', 'yellow', 'red', 'blue'}


# s = [x for x in range(10)]
# print(s)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = {x for x in range(10)}
# print(s)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} Порядок мнимый
# s = {x * x for x in range(10)}
# print(s)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}


# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = {x for x in numbers}
# print(s)  # {1, 2, 3, 4, 5, 6}
# s = {x for x in numbers if x % 2 == 0}  # {2, 4, 6}
# print(s)


# def to_set(par):
#     return set(par), len(set(par))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# s = {'banana', 'apple', 'orange'}
# if 'banana' in s:  # Проверяем наличие элемента в S
#     print('yes')  # yes
# else:
#     print('no')
# for i in s:
#     print(i, end=' ')  # banana orange apple


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r}
# print(a)  # {'bc_2', 'ab_1', 'ac_2', 'bc_1'} Будет произвольный порядок
# a = {i for i in r if 'a' not in i}
# print(a)  # {'bc_2', 'bc_1'}
#
# b = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# print(b) # {'Ac_2', 'Bc_2', 'Ab_1', 'Bc_1'}
#
#
# c = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A'+ i[1:])
#         else:
#             print('B'+ i[1:])
# print(c)


# s = {'banana', 'apple', 'orange'}
# s.add(4)  # Добавляем элемент во множество
# print(s)  # {'banana', 4, 'apple', 'orange'}
# s.remove(4)  # Удаляем элемент из множества
# print(s)  # {'orange', 'apple', 'banana'}
#
# if 5 in s:
#     s.remove(5) # Если есть 5 ,то удаляет ее
#
# s.discard(44) # Удаляет элемента по значению, пропуск,если его нету по умолчанию
# s.pop() # Удаляет первый элемент
# print(s)
# s.clear() # Очищает множество полностью
# print(s) # set()


# Операции над множествами
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a + b # ВЫДАСТ ОШИБКУ, СЛОЖИТЬ НЕЛЬЗЯ!
# print(a | b)  # Объединяет множества : {0, 1, 2, 3, 4}
# a |= b # Перезапишет "а" ,добавит элементы из "б"
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(len(s))  # 9
# print(min(s))  # 1
# print(max(s))  # 9
# print(sum(s))  # 45


# a = 'Hello'
# b = 'How are you'
# print(set(a) & set(b)) # {'e', 'H', 'o'} Выведет общие элементы

# drawing = {'Марина', 'Женя', "Света"}
# music = {'Костя', "Женя", "Илья"}
#
# one_hobby = drawing ^ music
# print('One hobby:', one_hobby)
# both_hobby = drawing & music
# print('Both hobby:', both_hobby)
# drawing = drawing - both_hobby
# print(drawing)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# # s.add('s') изменить frozenset уже нельзя


# Словарь (dict)

# a = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d) # {'one': 1, 'two': 2, 'three': 3}
# print(d['one']) # 1


# d = {'one': 1, 'two': 2}
# print(type(d))  # <class 'dict'>
# print(d) # {'one': 1, 'two': 2}
# d1 = dict(one=1, two=2) # КЛЮЧ В ВИДЕ ЧИСЛОВОГО ЗНАЧЕНИЯ бы не передалось
# print(d1) # {'one': 1, 'two': 2}
# print(type(d1))  # <class 'dict'>


# a = [1,2,3]
# # b = dict(a) Преобразовать список в словарь не получится!
# a = [
#     ('igor@gmail.com', 'igor'),
#     ('irina@gmail.com', 'irina'),
#     ('anna@gmail.com', 'Anna'),
# ]
# b = dict(a)
# print(b) # {'igor@gmail.com': 'igor', 'irina@gmail.com': 'irina', 'anna@gmail.com': 'Anna'}


# d = {i: i**2 for i in range(7)}  # Ключ: значение
# print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}


# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', 42: [2, 3, 5, 7]}  # Ключами не может быть изменяемый тип данных
# print(d)
# print(d[42][0])  # 2
# print(d[(1, 2.3)])  # 'Кортеж'
# d[(1, 2.3)] = 'Новое значение'
# print(d) # {0: 'text', 'one': 45, (1, 2.3): 'Новое значение', 42: [2, 3, 5, 7]}
# print('one' in d) # TRUE проверка ключа
# del d['one'] # Удалится и ключ и значение
# print('one' in d) # false


# d = {0: 'text', 'one': 45, (1, 2.3): 'Кортеж', 42: [2, 3, 5, 7]}  # Ключами не может быть изменяемый тип данных
# for key in d:
#     print(key,'->',d[key])  # Выведет построчно словарь


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)


# d ={}
# d[1] = input('->')
# d[2] = input('->')
# d[3] = input('->')
# d[4] = input('->')
# d = {i: input('->') for i in range(1,5)}
# print(d)
# delete = int(input('Какой элемент удалить: '))
# del d[delete]
# print(d)


# goods = {
#     '1': ['Core-I3-4330', 9, 4500],
#     '2': ['Core-I5-4350K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-I5-3450', 5, 6400],
# }
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2],'руб.', sep='')
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input('Введите кол-во товара: '))
#         goods[n][1] = qty
#     else:
#         break
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2],'руб.', sep='')
#


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['c'])
# value = d.get('f', 'Такого ключа нет')  # Получает значение по заданому ключу,даже если его нет
# print(value)
# print(d)
# n = d.keys()  # dict_keys(['a', 'b', 'c']) список ключей
# print(n)
# n = d.values()  # dict_values([1, 2, 3]) список значений
# print(n)
# n = d.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])
# print(n)
#
# for i in d.values():
#     print(i, end=' ')  # 1 2 3
# for i, j in d.items():
#     print(i, '->', j, end=' ') # a -> 1 b -> 2 c -> 3


# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d
# print(id(d), id(d2))  # ID будет одинаковый
#
# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print(id(d), id(d2))  # ID будет разный


# d = {'a': 1, 'b': 2, 'c': 3}
# # item = d.pop('b') # удаляет элемент из словаря по ключу, возвращает значение ключа
# print(d) # {'a': 1, 'c': 3}
# item2 = d.popitem() # Удаляет посленднюю пару ключ + значение и возвращает их
# print(item2)


# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.setdefault('f', 5)  # добавит ключ-значение, если его еще нету
# print(item)
# print(d)

#
# d = {'a': 1, 'b': 2, 'c': 3}
# d.update({'a':20,'w':10}) # если есть ключ, обновит его,если нет- добавит
# print(d) # {'a': 20, 'b': 2, 'c': 3, 'w': 10}


# x = {'a': 1, 'b': 2}
# y = {'c': 3, 'd': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y # более новый оператор для обьединения словарей, аналогичем двум строчкам выше
# print(z)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New-York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# print(new_d)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New-York'}
# d['location'] = d.pop('city')
# print(d)  # ...'location': 'New-York'}


# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'second': {
#         4: 'four',
#         5: 'five',
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t',y,':',a[x][y] )


# sales = {
#     'John': {
#         'N': 2132,
#         'S': 2313,
#         'E': 3214,
#         'W': 1242,
#     },
#     'Terry': {
#         'N': 3000,
#         'S': 2220,
#         'E': 6224,
#         'W': 4321,
#     },
#     'Anne': {
#         'N': 2000,
#         'S': 1220,
#         'E': 5224,
#         'W': 3221,
#     },
#     'Fiona': {
#         'N': 2200,
#         'S': 3215,
#         'E': 4400,
#         'W': 5000,
#     },
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ':', sales[x][y])
# name = input('Введите имя: ')
# region = input('Регион: ')
# print(sales[name], ':', sales[name][region])
# new_score = int(input('Новое значение: '))
# sales[name][region] = new_score
# print(sales[name])


# d = {'a': 1, 'b': 2, 'c': 3}
# w = {k: v for k, v in d.items()}
# print(w)
#
# d = {'a': 1, 'b': 2, 'c': 3}
# count = 0
# for i in d:
#     print(i,':', d[i])
#     count+=1
#     if count==2:
#         break


# value = int(input('-->'))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)


# d = {'a': 1, 'b': 2, 'c': 3,'d':4}
# value = list(d)
# print(value) # ['a', 'b', 'c', 'd']
# value = list(d.items())
# print(value) # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


# lst = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = {}
# s = None
# for i in lst:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)


# a = ['dec', 'jan', 'feb']
# b = [12, 1, 2]
# d = dict(zip(a, b))  # {'dec': 12, 'jan': 1, 'feb': 2}
# d = list(zip(a, b))  # [('dec', 12), ('jan', 1), ('feb', 2)]
# print(d)
# # zip работает только если элементов одинаково, лишние - отбросит


# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)  # чтобы зайти в список написали *
# print(a)  # (1, 2, 3, 4)
# print(b)  # ('a', 'b', 'c', 'd')


# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one,**two})  # {'apple': 0.4, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}


# data = ['a', 'b', 'c', 'd']
# for i in data:
#     print(i,end=' ') # a b c d
# print()
# for i in range(len(data)):
#     print(i, end=' ') # 0 1 2 3

# for j, i in enumerate(data):
#     print(j, ':', i,end=' ') # 0 : a 1 : b 2 : c 3 : d
# for j, i in enumerate(data,100):
#     print(j, ':', i,end=' ') # 100 : a 101 : b 102 : c 103 : d


# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for j, (i,v) in enumerate(d.items(), 100):
#     print(j, ':', i,'->',v)
# 100 : a -> 1
# 101 : b -> 2
# 102 : c -> 3
# 103 : d -> 4


# a = [1, 2, 3]
# b = [4, a, 5, 6]
# print(b)  # [4, [1, 2, 3], 5, 6]
# b = a + [4, 5, 6]
# print(b)  # [1, 2, 3, 4, 5, 6]
# b = [4, *a, 5, 6]
# print(b)  # [4, 1, 2, 3, 5, 6]


# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(3, 2))  # 5
# print(func(3, 4, 6))  # 13
# print(func())  # 0


# def func(*lst):
#     return {i: i for i in lst}
#
#
# print(func(1, 2, 3, 4))
# print(func('gray', (2, 17), 3.11, -4))


# def func(*lst):
#     sum = 0
#     count = 0
#     new_lst = []
#     for i in lst:
#         sum += i
#         count += 1
#     avarange = sum / count
#     print('Ср. ариф: ',avarange)
#     for j in lst:
#         if j < avarange:
#             new_lst.append(j)
#     print(new_lst)
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def func(a, *args):
#     return a, args
#
#
# print(func(2,3,4,5,'abc')) # (2, (3, 4, 5, 'abc'))


# def print_scores(student, *scores):
#     print("\nStudent Name:", student, end=", scores: ")
#     count = 0
#     for score in scores:
#         count += 1
#         if count != len(scores):
#             print(score, end=", ")
#         else:
#             print(score)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
# # ПЕРЕДАТЬ ЦИФРОВОЙ КЛЮЧ НЕЛЬЗЯ! (1=a,2=b,c=3) не сработает
# print(func()) # {}
# print(func(a='python')) # {'a': 'python'}


# def func(**data):
#     for key, value in data.items():
#         print(key,':',value)
#     print()
#
#
# func(name='Irina', surname='Sharma', age=22, phone=8932321212)
# func(name='Igor', surname='Wood',
#      email='igoejwj@mail.ru', country='Russia',
#      age=22, phone=8932321212)


# def func(**data):
#     for key, value in data.items():
#         my_dict[key] = value
#     return my_dict
#
#
# # Можно сокращенно написать так: my_dict.update(**data)
#
# my_dict = {'one': 'first'}
# print(func(k1=22, k2=31, k3=11, k4=91))
# print(func(name='Bob', age=31, weight=61, eyes_color='grey'))


# def func(*args, **data):
#     print(args, data)
#     print(args[0], data['k1'])
#
#
# func(4, 5, 6, 7, k1=22, k2=31, k3=11, k4=91)


# ОБЛАСТИ ВИДИМОСТИ (scope)

# name = 'Tom'  # глобальная переменная
# surname = ''  # Обьявляем ,чтобы программа не ругалась
#
#
# def gi():
#     global name, surname  # Объявляем name - глобальной
#     name = 'Sam'  # локальные переменные
#     surname = 'Fisher'
#     print('Hello', name, surname)  # Hello Sam Fisher
#
#
# def bye():
#     print('Good bye', name, surname)  # Good bye Sam
#
#
# gi()
# bye()


# i = 5
#
#
# def func(arg=i):  # Значение i возьмет выше
#     print(arg)
#
#
# i = 6
# func()  # Выведет 5


# def add_two(a):
#     x = 2  # "x" за пределами функции не существует
#
#     def add_some():
#         x = 3  # "х" перезапишется
#         return a + x
#
#
#     return add_some()
#
#
#
# print(add_two(3))


# import builtins
#
# name=dir(builtins)
#
# for t in name:
#     print(t)


# def outer_func(who):
#     def inner_func():
#         print('Hello,',who)
#
#     inner_func()
#
#
# outer_func('world')


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print('a=', a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t  # Выносит "t" как глобальную переменную
#     a = 30
#
#     def inner():
#         nonlocal a # Выносим "а" на уровень выше
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)

# a = 12
# a = 'a'
# print(a)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x=',x)
#
#     fn2()
#     print('fn1.x=', x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)  # [1, 7]


# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add = outer(5)
# print(add(10))  # 15
# add1 = outer(6)
# print(add1(10))  # 16
# print(outer(5)(10))  # 15


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = 'new' + b
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())  # (2, 'newline', [1, 2, 3, 4])

# s = 0


# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(c, b))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))


# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))


# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
#
# res1 = func('Moscow')
# res1()  # Moscow 1
# res1()  # Moscow 2
# res2 = func('Sochi')
# res2()  # Sochi 1
# res2()  # Sochi 2
# res1()  # Moscow 3


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print('A:', A(students))  # A: {'Alice': 98, 'Chris': 85}
# print('B:', B(students))  # B: {'David': 75}
# print('C:', C(students))  # C: {'Bob': 67, 'Ella': 54, 'Grace': 69}
# print('D:', D(students))  # D: {'Fiona': 35}


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())


# lambda (Анонимные функции)

# print((lambda x, y: x + y)(1, 2))  # 3
# print((lambda x, y: x + y)('a', 'b'))  # ab
#
# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x**2 + y**2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c + c  # Дали значение по умолчанию для "с"
#
# print(summ(10, 20, 30))  # 90
# print(summ(10, 20, ))  # 36
# print(summ()) # 9

# func = lambda *args: args
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8))  # (1, 2, 3, 4, 5, 6, 7, 8)
# print(func(1, 2, ))  # (1, 2)


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4) # В "с" лежит кортеж
#
# for i in c:
#      print(i('!!!,'))


# Вариант 1
# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))  # 45
# # Вариант 2
# # Аналог из функций
# def inc2(n):
#     def wrap(x):
#         return n + x
#
#     return wrap


# f1 = inc2(42)
# print(f1(3))  # 45

# # Вариант 3
# inc3 = (lambda n: lambda x: n+x)

# f2 = inc3(42)
# print(f2(3))  # 45

# # Вариант 4
# print((lambda n: lambda x: n+x)(42)(3))  # 45

# print((lambda i: lambda j: lambda k: i+j+k)(2)(4)(6))

# lst = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6},
# ]
# res = sorted(lst, key=lambda item: item['last name']) # Сортировка по ключу "ласт нейм"
# print(res)
# res1 = sorted(lst, key=lambda item: item['raiting'],reverse=True)
# print(res1)

# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 3, 'c': 7, }
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)  # lst.sort(key=lambda i: i[1]) Аналог для лямбды
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# print(a[0](1, 0))  # 1
# print(a[1](2, 3))  # -1
# print(a[2](2, 3))  # 6
# print(a[3](2, 3))  # 0.666

# a = {
#     'one': lambda x: x - 1,
#     'two': lambda x: x - 3,
#     'three': lambda x: x
# }
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
# }
#
# d[3]() # Среда

# m = lambda a, b: a if a > b else b
# print(m(1, 5))

# print((lambda a, b, c: a if a < b and a < c else b if b < a < c else c)(9, 8, 5))

# map(func, iterable), filter(func, iterable)

# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lst2 = list(map(mul, lst))
# print(lst2)

# Аналог
# lst = [2, 8, 12, -5, -10]
# print(list(map(lambda t: t * 2, lst)))  # [4, 16, 24, -10, -20]

# t = (2.88, -1.75, 100.03)
#
# # t2 = tuple(map(lambda x: int(x), t))
# # ИЛИ:
# t2 = tuple(map(int, t))
#
# print(t2)  # (2, -1, 100)

# area = [3.42323, 5.423412, 7.4324234, 5.654344, 1.5435345, 9.4324231]
#
# res = list(map(round, area, range(1, 6)))
# print(res)  # [3.4, 5.42, 7.432, 5.6543, 1.54353, 9.432423]
#
# # Для того чтобы сокращалось до 3-х символов после точки
# res = list(map(round, area, [3, 3, 3, 3, 3, 3]))
# print(res) # [3.423, 5.423, 7.432, 5.654, 1.544, 9.432]
#
# # print(round(3.312312, 3))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: (y, x), st, num))
# print(res) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
#
# res1 = dict(map(lambda x, y: (x, y), st, num))
# print(res1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x+y, l1, l2)))


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, I am func "func test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # Декорирующая функция
#     def func_wrapper():
#         print('*'*30)
#         func()
#         print('*'*30)
#
#     return func_wrapper
#
#
# @my_decorator  # Добавили декоратор
# def func_test(): # Декорируемая функция
#     print('Hello, I am func "func test"')
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())


# def numbers(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции: ',count)
#
#     return wrap
#
#
# @numbers
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print('Данные:', arg1,arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут:', first, last)
#
#
# print_full_name('igor', 'osokin')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут:', first, last)
#
#
# @args_decorator
# def print_full_name1(first, second, last):
#     print('Меня зовут:', first, second, last)
#
#
# print_full_name('igor', 'osokin')
# print()
# print_full_name1('igor', last='boy', second='osokin')


# def decor(arg1,arg2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor('Сумма:','+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность:','-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)  # Сумма: 5 и 2 =  7
# sub(5, 2)  # Разность: 5 и 2 = 3

# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#         return wrap
#     return decor
#
# @multiply(3)
# def return_num(num):
#     return num
#
# print(return_num(5))


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     return 'Некорректный тип данных'
#                     # raise TypeError()
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 'Doe'))


# def func1(a=None, b=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(b, end='')
#             func(*args)
#
#         return wrap
#
#     if a is None:
#         return my_decorator
#     else:
#         return my_decorator(a)
#
#
# @func1(b='Hello,')
# def hello(text):
#     print(text)
# 
#
# @func1
# def hello2(text):
#     print(text)
#
#
# hello('world!')
# hello2('Hi')

print('hello')