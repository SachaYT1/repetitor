f = open('KEGE 27 B 17916 (1).txt').readlines()
clusters = [[], [], [], [], []]

for i in f:
    p = list(map(float, i.split()))
    if p[0] > 12:
        clusters[0].append(p)
    elif p[1] > 14:
        clusters[1].append(p)
    elif p[1] > 9:
        clusters[2].append(p)
    elif p[1] > 5:
        clusters[3].append(p)
    else:
        clusters[4].append(p)

print(sum([len(i) for i in clusters]))

# print(*[1, 2, 3])

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def center(cluster):
    ans = -1
    minSm = 10 ** 9
    for p in cluster:
        sm = 0
        for p1 in cluster:
            sm += dist(p, p1)
        if sm < minSm:
            minSm = sm
            ans = p
    return ans


px = 0
py = 0

centers = []
for cluster in clusters:
    centers.append(center(cluster))

for c in centers:
    px += c[0]
    py += c[1]

px *= 10000 / len(centers)
py *= 10000 / len(centers)
print(int(px), int(py))

