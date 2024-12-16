f = open('17_1993.txt').readlines()
a = []
for i in f:
    a.append(int(i))

count = 0
maxSum = []
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        num1 = a[i]
        num2 = a[j]
        sumPair = num1 + num2
        if (abs(sumPair) % 3 == 0 and abs(sumPair) % 6 != 0) and (abs(num1 * num2) % 10 == 8):
            count += 1
            maxSum.append(sumPair)

print(count, max(maxSum))