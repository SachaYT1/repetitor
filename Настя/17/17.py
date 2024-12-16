f = open('17 (4).txt').readlines()
a = []
for i in f:
    a.append(int(i))

max17 = -10**6
for elem in a:
    if elem % 17 == 0 and elem > max17:
        max17 = elem

maxSumPair = -10**6
countPair = 0
for i in range(len(a) - 1):
    num1 = a[i]
    num2 = a[i + 1]
    if num1 + num2 > max17:
        countPair += 1
        if num1 + num2 > maxSumPair:
            maxSumPair = num1 + num2

print(countPair, maxSumPair)