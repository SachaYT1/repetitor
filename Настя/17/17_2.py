f = open('17_(2).txt').readlines()
a = []
for i in f:
    a.append(int(i))

count = 0
maxSum = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        num1 = a[i]
        num2 = a[j]
        if ((num1 + num2) % 18 == 0) + ((num1 * num2) % 18 == 0) == 1:
            count += 1
            if num1 + num2 > maxSum:
                maxSum = num1 + num2
print(count, maxSum)