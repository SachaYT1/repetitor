data = []

for s in open('KEGE 27 B 17916 (1).txt'):
    x, y = [float(c) for c in s.split()]
    data.append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 -x2) ** 2 + (y1 - y2) **2) ** 0.5

def getCluster(p):
    cluster = [p1 for p1 in data if dist(p, p1) < 0.2]
    if len(cluster) > 0:
        for p1 in cluster:
            data.remove(p1)
        next_cluster = [getCluster(p1) for p1 in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster


clusters = []

while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    clusters.append(cluster)

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]

centers = [center(kl) for kl in clusters]

px = sum(x for x, y in centers) / len(centers)
py = sum(y for x, y in centers) / len(centers)

print(int(px * 10000), int(py * 10000))