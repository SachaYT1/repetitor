
def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base


s = []
for n in range(2, 10_001):
    n3 = perevod(n, 3)
    n3 = ''.join(sorted(n3, reverse=True))
    n3 = n3 + n3[0]
    r = int(n3, 3)
    if r < 1200:
        s.append(r)
print(max(s))



