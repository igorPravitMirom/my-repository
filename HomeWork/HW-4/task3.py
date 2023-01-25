a = [int(input('-->')) for i in range(int(input('n= ')))]
print('Элементы с четными индексами: ',end='')
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')
