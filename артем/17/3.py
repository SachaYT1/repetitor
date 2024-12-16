f = open('17 (3).txt').readlines()
a = []
for i in f:
    a.append(int(i))

min8 = 10000
for num in a:
    if (100 <= abs(num) <= 999) and (abs(num) % 10 == 8):
        if num < min8:
            min8 = num


count = 0
maxSum = []
for i in range(0, len(a) - 2):
    num1 = a[i]
    num2 = a[i + 1]
    num3 = a[i + 2]
    if ((num1 ** 2 > min8 ** 2) + (num2 ** 2 > min8 ** 2) + (num3 ** 2 > min8 ** 2)) == 2:
        if (100 <= abs(num1) <= 999) or (100 <= abs(num2) <= 999) or (100 <= abs(num3) <= 999):
            count += 1
            maxSum.append(num1 + num2 + num3)
print(count, max(maxSum))
