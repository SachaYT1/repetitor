def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base


a = []
maxR = -1000
for n in range(1, 10000):
    num3 = perevod(n, 3)
    num3 = sorted(num3, reverse=True)
    num3 = ''.join(num3)
    num3 = num3 + num3[0]
    r = int(num3, 3)
    if r < 1200:
        a.append(r)
        if r > maxR:
            maxR = r

print(max(a), maxR)

