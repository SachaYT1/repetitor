from itertools import product

a = product('01234', repeat=6)

print(ord('1'))



k = 0
for i in a:
    s = ''.join(i)
    if s[0] != '0' and s[0] != '1' and s[-1] not in '34':
        k += 1

print(k)