import random as r
mas = [r.randint(0,100) for i in range(10)]
print(mas)
minimum = min(mas)
print('Min: ', minimum)
ind = mas.index(min(mas))
print('Index min: ',ind)
print(mas[ind+1:])