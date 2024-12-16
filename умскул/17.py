f = open('17.4.txt').readlines()
a = [int(elem) for elem in f]


countPairs = 0
maxMultiply = -10 ** 7

for i in range(len(a) - 1):
    lastDigit1 = a[i] % 10
    lastDigit2 = a[i + 1] % 10
    if (lastDigit1 == lastDigit2) and (lastDigit1 % 2 == 0):
        countPairs += 1
        maxMultiply = max(maxMultiply, abs(a[i] * a[i + 1]))

print(countPairs, maxMultiply)