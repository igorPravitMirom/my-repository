# print(6+2)
# print(6/2) #3.0 выдаст
# print(6//2) #3
# print(7//2) #3
# print(7**2)
# print(7%2)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# num1 = 5
# num2 = 7
# num3 = 3
# print("Сумма:", num1 + num2 + num3)
# print("Произведение:", num1 * num2 * num3)
# print("Среднее арифметическое:", (num1 + num2 + num3) / 3)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15

# num = 9753
# reverse= num %10
# num //=10
# reverse*=10
# reverse+=num %10
# num //=10
# reverse*=10
# reverse+=num %10
# num //=10
# reverse*=10
# reverse+=num %10
# print(num)
# print(reverse)

# num1 = '2'
# num2 = 3
# res = num1 + str(num2)  # преобразовали num2 из числа в строку
# res2 = int(num1)
# print(res2)
# num3 = '2.5'
# num4 = 2
# # print(int(num3)) ,будет ошибка! ОН не преобразует дробную строку в число
# print(float(num3) + num4)

# print(int(3.8)) #3
# print(round(3.8)) #4 - округление по законам математики
# print(round(3.891, 2)) # округляет до 2-х символов после точки

# name = 'Igor'
# age = 25
# print("Меня зовут", name + ".Мне", age, "лет")  # Убрали пробел после name
# print("Меня зовут", name, ".Мне", age, "лет", sep="--")  # сделали между словами вместо пробела "--"
# print("Я учу Python",
#       end=" ")  # енд говорит чем заканчивается строка, щас убираем перенос строки итог: "Я учу Python сейчас"
# print("сейчас")

# Ввод данных
# name = input("Введите ваше имя: ")
# print(name)

# num = input("Введите число: ")
# step = input("Введите степень: ")
# res = int(num) ** int(step)
# print("Число:",num,"в степени:",step,"равно:",res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 6 True = 1 False = 0
# print(bool(""))  # Преобразует пустую строку в bool значение
# print(bool(" "))  # есть пробел -  TRue
# print(bool(1))  # True
# print(bool(0))  # False
# print(bool(None))  # False None - ничего
# test = None
# print(test) #None

# Операторы сравнения
# print(7 == 7) #True
# print(2+5 == 7) #True
# print(2+5 <= 7) #True
# print(9 >= 7) #True
# print(9 != 7) #True
# print(2<4<9) #True проверяет по очереди слева направо 2<4 потом 4<9 , если оба True , то выражение тоже true

# Логические операторы
# && = and
# || = or
# not - не
# print(5-3 == 2 and 1+3==4) # True
# a = True
# b = not a
# print(b) # False

# IF Else
# num = 5
# if num < 10:
#     num += 1
#     print(num)  # 6 астояние слева обязательно

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# elif age <=18:
#     print("Вам меньше 18 лет")
# else:
#     print("Доступ запрещен")
# side1 = int(input("Введите первую сторону:"))
# side2 = int(input("Введите вторую сторону:"))
# side3 = int(input("Введите третью сторону:"))
# if side1 == side2 and side2 == side3:
#     print("Треугольник равносторонний")
# elif side1==side2 or side1==side3 or side2==side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели(цифрой): "))
# if day>=1 and day<=5: #Можно написать так: 1 <= day <=5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     elif day == 2:
#         print("Вторник")
#     elif day == 3:
#         print("Среда")
#     elif day == 4:
#         print("Четверг")
#     elif day == 5:
#         print("Пятница")
# elif day ==6 or day==7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     elif day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")

# season = int(input("Введите номер месяца(цифрой): "))
# if season == 12 or 1<= season <=2:
#     print("Зима")
# elif 3<= season <=5:
#     print("Весна")
# elif 6 <= season <= 8:
#     print("Лето")
# elif 9 <= season <= 11:
#     print("Осень")
# else:
#     print("Такого времени года не существует для вашего месяца")

voron = int(input("Введите количество ворон(цифрой): "))
if 0 <= voron <= 9:
    if voron == 1:
        n = "ворона"
    elif 2 <= voron <= 4:
        n = "вороны"
    else:
        n = "ворон"
    print("На ветке:", voron, n)
else:
    print("Ошибка ввода")
