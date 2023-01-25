from random import randint

w, h = 6, 6
matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
newMatrix = [[0 for j in range(h)] for k in range(w)]
lit = 0
big = 1
# Для новой матрицы
# newMatrix[0], newMatrix[1] = matrix[1], matrix[0]
# newMatrix[2], newMatrix[3] = matrix[3], matrix[2]
# newMatrix[4], newMatrix[5] = matrix[5], matrix[4]
while lit < h:
    newMatrix[lit], newMatrix[big] = matrix[big], matrix[lit]
    lit += 2
    big += 2
# Для старой матрицы
for row in matrix:
    for x in row:
        print(x, end='\t\t')
    print()
print()
for row in newMatrix:
    for x in row:
        print(x, end='\t\t')
    print()
