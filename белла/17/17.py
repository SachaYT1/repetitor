f = open('17 (6).txt').readlines()
a = []
for i in f:
    a.append(int(i))

num42 = -10**10
b = []
for num in a:
    if abs(num) % 100 == 42:
        if 1000 <= abs(num) <= 9999:
            if num > num42:
                num42 = num

count = 0
max3 = -10**10
for i in range(len(a) - 2):
    num1 = a[i]
    num2 = a[i + 1]
    num3 = a[i + 2]
    if (abs(num1) % 100 == 42 and 1000 <= abs(num1) <= 9999) + \
            (abs(num2) % 100 == 42 and 1000 <= abs(num2) <= 9999) + \
            (abs(num3) % 100 == 42 and 1000 <= abs(num3) <= 9999) >= 2:
        if num1 + num2 + num3 > num42:
            count += 1
            if num1 + num2 + num3 > max3:
                max3 = num1 + num2 + num3
print(count, max3)
