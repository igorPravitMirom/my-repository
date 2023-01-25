posl = [1, 3, 4, 5, 2, 4, 6, 1, 2, 7, 1, 1]
answ = []
for i in posl:
        if posl.count(i) == 1: answ.append(i)
print(*answ)