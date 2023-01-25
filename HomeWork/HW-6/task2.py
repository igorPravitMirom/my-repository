from random import randint

w, h = 4, 3
matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
newMatrix = [[0 for j in range(h)] for k in range(w)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        newMatrix[j][i] = matrix[i][j]
for row in matrix:
    for x in row:
        print(x, end='\t\t')
    print()
print()
for row in newMatrix:
    for x in row:
        print(x, end='\t\t')
    print()
