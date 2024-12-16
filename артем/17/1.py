f = open('17.txt').readlines()
a = []
for num in f:
    a.append(int(num))

sum11 = 0
n11 = 0
for num in a:
    if num % 11 == 0:
        sum11 += num
        n11 += 1

sr11 = sum11 / n11

print(-211 % 100)

count = 0
maxTr = -10**6
for i in range(0, len(a) - 2):
    num1 = a[i]
    num2 = a[i + 1]
    num3 = a[i + 2]
    if (abs(num1) % 100 == 11 or abs(num2) % 100 == 11 or abs(num3) % 100 == 11) and \
            (num1 + num2 + num3) / 3 > sr11:
        count += 1
        if (num1 + num2 + num3) > maxTr:
            maxTr = num1 + num2 + num3
print(count, maxTr)
