import random as r
mas = [r.randint(-100,100) for i in range(10)]
print('Изначальный список: ',mas)
mas.sort()
mas.reverse()
print('Конечный список: ',mas)
