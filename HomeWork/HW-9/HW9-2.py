total_students = int(input('Введите количество студентов: '))
d = {}
count = 1
total_score = 0
if total_students > 0:
    for i in range(1, total_students + 1):
        print(count, '-й', sep='', end=' ')
        name = input('студент: ')
        score = int(input('Балл: '))
        d[name] = score
        total_score += score
        count += 1
    avarange_score = round((total_score / len(d)), 2)
    best_list = []
    for key in d:
        if d[key] > avarange_score:
            best_list.append(key)
    print('Средний балл:', avarange_score)
    print('Студенты с баллом,выше среднего: ', ','.join(best_list))
else:
    print('Вы ввели некорректное число студентов!')
