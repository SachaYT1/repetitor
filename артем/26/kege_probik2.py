f = open('KEGE 18030.txt')

n = int(f.readline())

a = []
for i in range(n):
    number = int(f.readline())
    a.append(number)

a.sort()


flag = True

countLevels = 0
minSum = 0
i = 1
countCards = 0
while (flag):
    if n - countCards >= i:
        pass
    else:
        break

    countCards += i
    i = i + 1
    countLevels += 1

minSum = sum(a[0:countCards])

print(countLevels, minSum)
