f = open('9.txt').readlines()

count = 0
for i in f:

    a = list(map(int, i.split()))
    a.sort()
    if (a[0] * a[3] == a[1] * a[2]) and (a[2] ** 2 > a[0] * a[3]):
        count += 1
print(count)

