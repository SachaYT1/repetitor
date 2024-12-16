from itertools import product
a = product('БИКНОПР', repeat=6)

n = 1
ans = 0
for i in a:
    s = ''.join(i)
    if s.count('О') == 3 and len(set(s)) == 4:
        ans = n
    n += 1
print(ans)
