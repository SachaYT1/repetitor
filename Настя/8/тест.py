from itertools import product
a = product('01', repeat=20)
b = dict()
for i in range(0, 20 + 1):
    b[i] = 0
for i in a:
    s = ''.join(i)
    b[s.count('0')] += 1
print(b)