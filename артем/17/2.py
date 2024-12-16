f = open('17 (2).txt').readlines()
a = []
for i in f:
    a.append(int(i))

max21 = 0
for i in a:
    if (i % 21 == 0) and (i > max21):
        max21 = i

count = 0
minSum = []
for i in range(0, len(a) - 1):
    num1 = a[i]
    num2 = a[i + 1]
    if (num1 > max21 or num2 > max21):
        count += 1
        minSum.append(num1 + num2)
print(count, min(minSum))