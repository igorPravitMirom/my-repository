print("Данная программа найдет максимальное из введенных вами трех чисел")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
print("Максимальное число из  ваших трех(", num1, num2, num3, ") ,будет: ", end='')
print(num1 if (num1 > num2 and num1 > num3) else num2 if (num2 > num1 and num2 > num3) else num3)
