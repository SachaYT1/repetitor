from itertools import product, permutations
a = product('0123456789AB', repeat=5)
count = 0
for i in a:
    s = ''.join(i)
    if s[0] != '0' and s.count('7') == 1 and (
        s.count('9') + s.count('A') + s.count('B')
    ) <= 3:
        count += 1
print(count)