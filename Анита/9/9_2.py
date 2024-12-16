f = open('09.txt').readlines()
count = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    if (a[4] ** 2 > a[0] * a[1] * a[2] * a[3]) and (a[3] + a[4] > 2 * (a[0] + a[1] + a[2])):
        count += 1
print(count)