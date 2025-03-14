f = open('KGE 17.txt').readlines()
a = []
for num in f:
    a.append(int(num))

num55 = 0

for num in a:
    if abs(num) % 55 == 0:
        num55 = max(num, num55)


count = 0
maxSum = -10**6
for i in range(len(a) - 1):
    num1 = a[i]
    num2 = a[i + 1]
    if (num1 % 5 == 0 or num2 % 5 == 0):
        if (num1 + num2 <= num55):
            count += 1
            maxSum = max(num1 + num2, maxSum)
print(count, maxSum)

