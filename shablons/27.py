'''
тоже достаточно шаблонная штука, заходим в эксельку строим кластеры, потом распределяем по массивам.
по сути не шаблон - только распределение по кластерам (первый цикл) по очевидным причинам
'''


f = open('KEGE 27 B 17916.txt').readlines()

clusters = [[], [], [], [], []]

for i in f:
    p = list(map(float, i.split()))
    if p[0] > 12:
        clusters[0].append(p)
    elif p[1] > 13:
        clusters[1].append(p)

    elif p[1] > 9:
        clusters[2].append(p)
    elif p[1] > 5:
        clusters[3].append(p)
    else:
        clusters[4].append(p)

print(sum([len(a) for a in clusters]))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def center(cluster):
    sumDist = 10**9
    ans = -1
    for p in cluster:
        sm = 0
        for p1 in cluster:
            sm += dist(p, p1)
        if sm < sumDist:
            sumDist = sm
            ans = p
    return ans

centers = []
for cluster in clusters:
    centers.append(center(cluster))

print(centers)

px = 0
py = 0
for c in centers:
    px += c[0]
    py += c[1]

px *= 10000 / len(centers)

py *= 10000 / len(centers)

print(int(px), int(py))

