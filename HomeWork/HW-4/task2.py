a = [1, 3, 4, 5, 2, 4, 6, 1, 2, 7, 1, 1]
for i in range(len(a)):
    for j in range(len(a)):
        #print('j=',j,'i=',i)
        if i != j and a[i] == a[j]: # 0-0,0-1... / j=7 i=0
            break
    else:
        print(a[i], end=' ')
