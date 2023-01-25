# Вариант 1


def square(a, b, c):
    def func_result(one, two):
        return one * two

    s = 2 * (func_result(a, b) + func_result(b, c) + func_result(a, c))
    return s


print(square(2, 4, 6))
print(square(5, 8, 2))
print(square(1, 6, 8))


# Вариант 2
print()


def square(a, b, c):
    s = 0

    def func_result(one, two):
        nonlocal s
        s += one * two

    func_result(a, b)
    func_result(a, c)
    func_result(c, b)
    return 2 * s


print(square(2, 4, 6))
print(square(5, 8, 2))
print(square(1, 6, 8))
