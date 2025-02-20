a = set()
for i in range(1, 1000):
    a.add(i)
d = set()
b = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
c = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
for x in range(1, 1000):
    f = (not(x in a) or (x in b)) and (not(x in c) or not(x in a))
    if f:
        d.add(x)
print(d)