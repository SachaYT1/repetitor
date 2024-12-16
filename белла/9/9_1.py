f = open('9 (1).txt').readlines()

ans = 0
n = 0
for i in f:
    n += 1
    a = list(map(int, i.split()))
    b = set(a)

    if len(b) == 5:
        a.sort()
        if (a[0] + a[-1]) ** 2 > a[1] * a[2] * a[3]:
            ans += n
print(ans)