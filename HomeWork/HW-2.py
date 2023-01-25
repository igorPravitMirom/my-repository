money = int(input("Введите количество копеек от 0 до 100(цифрой): "))
if 0 <= money <= 100:
    if money == 2 or money == 3 or money == 4 or money % 10 == 2 or money % 10 == 3 or money % 10 == 4:
        a = "копейки"
    elif money == 1 or (money > 20 and money % 10 == 1):
        a = "копейка"
    else:
        a = "копеек"
print("У вас:", money, a)
