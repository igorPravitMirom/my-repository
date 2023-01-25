i = 0
while i < 5:
    j = 0
    while j < 16:
        if i % 2 == 0:
            print('+', end='')
        else:
            print('-', end='')
        j += 1
    print()
    i += 1
