from random import randint

w, h = 6, 6
matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
newMatrix = [[0 for j in range(h)] for k in range(w)]
oneLineMatrix = [randint(0, 10) for x in range(w)]
n = 1
# Для новой матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if n % 2 == 0:
            newMatrix[j][i] = matrix[j][i]
        else:
            newMatrix[j][i] = oneLineMatrix[i]
        n += 1
# Для старой матрицы
for row in matrix:
    for x in row:
        print(x, end='\t\t')
    print()
print(oneLineMatrix)
print()
for row in newMatrix:
    for x in row:
        print(x, end='\t\t')
    print()
