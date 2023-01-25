tpl = ('ab', 'abcd', 'cde', 'abc', 'def')
search = input('Введите какую строку ищите в кортеже: ')
if search in tpl:
    print('YES')
else:
    print('NO')