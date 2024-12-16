f = open('17 (4).txt').readlines()
a= []
for i in f:
    a.append(int(i))

max42 = -10**6
b = []
for num in a:
    if abs(num) % 100 == 42 and num > max42:
        b.append(num)
        max42 = num

count = 0
maxTriple = []
for i in range(len(a) - 2):
    num1 = a[i]
    num2 = a[i + 1]
    num3 = a[i + 2]
    if (abs(num1) % 100 == 42) + (abs(num2) % 100 == 42) \
        + (abs(num3) % 100 == 42) >= 2:
        if num1 * num2 * num3 > max42 ** 2:
            count += 1
            maxTriple.append(num1 * num2 * num3)
print(count, max(maxTriple))

print()