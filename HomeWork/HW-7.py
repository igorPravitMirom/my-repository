lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
simple_num_list = []
not_simple_num_list = []
print('Изначальный список: ',lst)
for i in lst:
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        simple_num_list.append(i)
    else:
        not_simple_num_list.append(i)
# print('Минимальное среди простых чисел: ', min(simple_num_list))
# print('Максимальное среди не простых:', max(not_simple_num_list))
print('Вносим изменения')
ad = 12312