countS = int(input("Введите число символов: "))
typeS = input("Введите тип символа: ")
orientation = int(input("Виды ориентации:\n 0-горизонтальная \n 1-вертикальная \n Введите номер вида ориентации: "))
string = ''
i = 0
while i < countS:
    string += typeS
    i += 1
if orientation == 0:
    print(string)
elif orientation == 1:
    j = 0
    while j < countS:
        print(typeS)
        j += 1
