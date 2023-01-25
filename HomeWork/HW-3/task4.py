while True:
    print('Выберите операцию:\n\
    1 - \"r\" - применяет унарный минус к числу \n\
    2 - \"+\" - сложение \n\
    3 - \"-\" - вычитание \n\
    4 - \"/" - деление \n\
    5 - \"*\" - умножение \n\
    6 - \"%\" - деление по модулю(остаток от деления) \n\
    7 - \"<\" - минимальное из двух чисел \n\
    8 - \">\" - максимальное из двух чисел\n\
    9 - \"quit\" - прекратить пользование калькулятором')
    operation = input("Введите номер операции: ")
    if operation == '9':
        print('Спасибо за пользование!До свидания')
        break
    num1 = int(input("Введите первое число: "))
    if operation == '1':
        print('Результат смены знака у числа(', num1, '),будет:', -int(num1))
    num2 = int(input("Введите второе число: "))
    if operation == '2':
        print(num1, '+', num2, '=', int(num1) + int(num2))
    elif operation == '3':
        print(num1, '-', num2, '=', int(num1) - int(num2))
    elif operation == '4':
        if num2 == 0:
            print('К сожалению всей математики, на ноль делить нельзя')
        else:
            print(num1, '/', num2, '=', int(num1) / int(num2))
    elif operation == '5':
        print(num1, '*', num2, '=', int(num1) * int(num2))
    elif operation == '6':
        print('Остаток от деления числа:', num1, 'на число:', num2, 'будет равен:', int(num1) % int(num2))
    elif operation == '7':
        if int(num1) < int(num2):
            print(num1, '-наименьшее из двух чисел')
        elif int(num1) == int(num2):
            print(num1, '=', num2, 'числа равны')
        else:
            print(num2, '-наименьшее из двух чисел')
    elif operation == '8':
        if int(num1) > int(num2):
            print(num1, '-наибольшее из двух чисел')
        elif int(num1) == int(num2):
            print(num1, '=', num2, 'числа равны')
        else:
            print(num2, '-наибольшее из двух чисел')
    print()
