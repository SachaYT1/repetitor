from itertools import product, permutations

a = product('БИКНОПР', repeat=6)
n = 0
ans = 0
for i in a:
    s = ''.join(i)
    b = set(s)
    n += 1
    if s.count('О') == 3 and len(b) == 4:
        ans = n
print(ans)
