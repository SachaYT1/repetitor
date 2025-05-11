f = open('kege_putniki.txt')

n, k = map(int, f.readline().split())

paths = []
for i in range(n):
    path = list(map(int, f.readline().split()))

    paths.append(path)


paths.sort()


d = {
    1: 0
}

for start, end, coins in paths:
    if start in d and coins + d[start] <= k:
        if end not in d:
            d[end] = coins + d[start]
        else:
            d[end] = min(d[end], coins + d[start] )

print(max(d.keys()))
print(k - d[max(d.keys())])
