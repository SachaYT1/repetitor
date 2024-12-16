f = open('17 (8).txt').readlines()
a = []
for i in f:
    a.append(int(i))

sr_arifm = sum(a) / len(a)

sum_max = -10**10
count = 0
for i in range(1, len(a) - 2):
    num1 = a[i - 1]
    num4 = a[i + 2]

    num2 = a[i]
    num3 = a[i + 1]

    if num2 * num3 > num1 * num4:
        if num2 + num3 > sum_max:
            sum_max = num2 + num3
        if (num2 > sr_arifm) + (num3 > sr_arifm) >= 1:
            count += 1

print(sum_max, count)

