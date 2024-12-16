f = open('17 (5).txt').readlines()
a = []
for i in f:
    a.append(int(i))

max25 = -10 ** 6

for elem in a:
    if abs(elem) % 100 == 25 and elem > max25:
        max25 = elem

countTriple = 0
maxSumTriple = -10**6
for i in range(len(a) - 2):
    num1 = a[i]
    num2 = a[i + 1]
    num3 = a[i + 2]
    if (999 < abs(num1) < 10000) + (999 < abs(num2) < 10000) + (999 < abs(num3) < 10000) <= 2:
        if num1 + num2 + num3 <= max25:
            countTriple += 1
            if num1 + num2 + num3 > maxSumTriple:
                maxSumTriple = num1 + num2 + num3

print(countTriple, maxSumTriple)