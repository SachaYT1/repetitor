f = open('17 (7).txt').readlines()
a = []
for i in f:
    a.append(int(i))

num17 = -10**10
for num in a:
    if abs(num) % 100 == 17:
        if 10000 <= num <= 99999:
            if num > num17:
                num17 = num

count = 0
min3 = 10**10
for i in range(len(a) - 2):
    num1 = a[i]
    num2 = a[i + 1]
    num3 = a[i + 2]
    if (abs(num1) % 100 == 17) + (abs(num2) % 100 == 17) + \
            (abs(num3) % 100 == 17) >= 1:
        if abs(num1) + abs(num2) + abs(num3) <= num17:
            count += 1
            if num1 + num2 + num3 < min3:
                min3 = num1 + num2 + num3
print(count, min3)
