f = open('9.txt').readlines()
count = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    if (a[4] + a[0]) ** 2 > a[1]  ** 2 + a[2] ** 2 + a[3] ** 2:
        count += 1
print(count)