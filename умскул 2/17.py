f = open('17.4 (1).txt').readlines()
a = [int(x) for x in f]
print(a)

countPairs = 0
maxAbsSumPair = -10**7
for i in range(len(a) - 1):
    digit1 = abs(a[i]) % 10
    digit2 = abs(a[i + 1]) % 10
    if (digit1 == digit2) and digit1 % 2 == 1:
        countPairs += 1
        maxAbsSumPair = max(maxAbsSumPair, abs(a[i]) + abs(a[i + 1]))

print(
    countPairs, maxAbsSumPair
)
