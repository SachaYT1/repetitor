f = open('kege_dosrok.txt')
n = int(f.readline())

a = []
for i in range(n):
    length = int(f.readline())
    a.append(length)

a.sort()


countMax = 1
lengthMax = 0
for i in range(1, len(a)):
    minBox = a[i]
    currentBox = a[i]
    indx = i + 1
    count = 1
    while (indx < len(a)):
        if a[indx] - currentBox >= 9:
            currentBox = a[indx]
            count += 1
        indx += 1
    if count >= countMax:
        countMax = count
        lengthMax = minBox
    else:
        break
    
print(countMax, lengthMax)
