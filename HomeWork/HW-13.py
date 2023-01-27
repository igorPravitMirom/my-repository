def decorator(function_to_decorate):
    def wrap(*args):
        long = (len(args))
        summa = function_to_decorate(*args)
        print('Среднее арифметическое чисел:', *args, '=', (summa / long))
        print('Количество чисел:', long)

    return wrap


@decorator
def print_full_name(*args):
    summa = 0
    for i in args:
        summa += i
    print("Сумма чисел:",*args,'=', summa)
    return summa


print_full_name(2, 3, 3, 4)
