from itertools import product

a = product('0..9AB', repeat=5)
for i in a:
    s = ''.join(i)
    s.count('7') == 1