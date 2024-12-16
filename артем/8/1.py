from itertools import product, permutations
a = product('БИКНОПР', repeat=6)
n = 1
b = []

for i in a:
    s = ''.join(i)
    if s.count('О') == 3 and len(set(s)) == 4:
        b.append([n, s])
    n += 1
print(b[-1])
