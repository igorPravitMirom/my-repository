import random as r
mas = [r.randint(0,100) for i in range(10)]
print(mas)
maximum = max(mas)
ind = mas.index(max(mas))
print('Max:',max(mas))
del(mas[ind])
mas.insert(0, maximum)
print(mas)