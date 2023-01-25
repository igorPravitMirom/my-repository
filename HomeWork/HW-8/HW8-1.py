def my_function(tpl):
    max_list = []
    for i in tpl:
        if i % 13 == 0 and i > 0:
            max_list.append(i)
    if len(max_list)>0:
        return max(max_list)
    else:
        return 'no such numbers'


print(my_function((2, 7, 0, 3, 1, 5, -13)))
print(my_function((2, 7, 0, 3, 1, 5, -13, 13)))
print(my_function((13, 26,)))
print(my_function((99, 99, 100, 34, -39)))
print(my_function((99, 39, 99, 100, 34)))
