clustersA = [[], []]

for s in open(...):
    x, y = [float(c) for c in s.split()]
    if x < ...:
        clustersA[0].append([x, y])
    else:
        clustersA[0].append([x, y])


clustersB = [[], [], []]

...

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl) 
        m.append([sm, p])
    return min(m)