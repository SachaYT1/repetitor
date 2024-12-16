f = open('9 (4).txt').readlines()
ans = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    if (a[0] + a[2]) == 180 and (a[1] + a[3] == 180) and \
        (a[0] == a[1]):
        ans += 1
print(ans)
