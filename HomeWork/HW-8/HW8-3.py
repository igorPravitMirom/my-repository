tpl = input('Введите по порядку,без пробелов,элементы кортежа:')
tpl = tuple(tpl)
new_list = []
for i in tpl:
    if i not in new_list:
        new_list.append(i)
for j in new_list:
    print('Количество ', j, '=', tpl.count(j))
