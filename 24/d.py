f = open('dosrok.txt')

n = int(f.readline())

a = []
for i in range(n):
    length = int(f.readline())
    a.append(length)

a.sort()

countMax = 1
ansBox = 0
for i in range(n):
    smallestBox = a[i]
    currentBox = a[i]
    count = 1
    for j in range(i + 1, n):
        if a[j] - currentBox >= 9:
            count += 1
            currentBox = a[j]

    if count >= countMax:
        countMax = count
        ansBox = max(smallestBox, ansBox)


print(countMax, ansBox)