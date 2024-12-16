s = open('24_18284.txt').read()
lpos = []
opos = []
vpos = []
epos = []

k = 0
for c in s:
    if c == 'L':
        lpos.append(k)
    if c == 'O':
        opos.append(k)
    if c == 'V':
        vpos.append(k)
    if c == 'E':
        epos.append(k)
    k += 1

llen, olen, vlen, elen = len(lpos), len(opos), len(vpos), len(epos)
l, o, v, e = 0, 0, 0, 0

while opos[o] < lpos[l]:
    o += 1
while vpos[v] < opos[o]:
    v += 1
while epos[e] < vpos[v]:
    e += 1
size = epos[e] - lpos[l] + 1

while l < llen and o < olen and v < vlen and e < elen:
    l += 1
    while l < llen and o < olen and opos[o] < lpos[l]:
        o += 1
    while o < olen and v < vlen and vpos[v] < opos[o]:
        v += 1
    while v < vlen and e < elen and  epos[e] < vpos[v]:
        e += 1
    if l < llen and o < olen and v < vlen and e < elen:
        size = min(size, epos[e] - lpos[l] + 1)
print(size)