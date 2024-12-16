f = open('17_1999.txt').readlines()
a = []
for i in f:
    a.append(int(i))

count = 0
minSrArifm = 10 ** 6
for i in range(0, len(a) - 2):
    num1 = a[i]
    num2 = a[i + 1]
    num3 = a[i + 2]
    if (num1 % 12 == 0 or num2 % 12 == 0 or num3 % 12 == 0) and \
        (num1 % 3 == 0 and num2 % 3 ==0 and num3 % 3 == 0):
        count += 1
        minSrArifm = min(minSrArifm, (num1 + num2 + num3) / 3)

print(count, minSrArifm)