f = open('6B.txt').readlines()

clusters = [[], [], []]

for i in f:
    p = list(map(float, i.split()))
    x = p[0]
    y = p[1]
    if x > 0 and y < x + 4:
        clusters[0].append(p)
    elif x < 0 and y < 3.5:
        clusters[1].append(p)
    else:
        clusters[2].append(p)

print(sum([len(i) for i in clusters]))


def dist(p1, p2):
    x1, y1, x2, y2 =  *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def center(cluster):
    ans = -1
    minSum = 10 ** 9

    for p in cluster:
        sm = 0
        for p1 in cluster:
            sm += dist(p, p1)

        if sm < minSum:
            minSum = sm
            ans = p

    return ans

centers = []
for cluster in clusters:
    centers.append(center(cluster))

px = 0
py = 0
for c in centers:
    px += c[0]
    py += c[1]

px *= 100_000 / len(centers)
py *= 100_000 / len(centers)
print(int(px), int(py))