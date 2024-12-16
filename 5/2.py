def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base


a = '12345'
print(a[-1] + a[1:-1] + a[0])


b = []
for n in range(1, 10000):
    num4 = perevod(n, 4)
    if n % 3 == 0:
        num4 = num4[-1] + num4[1:-1] + num4[0] + '1'
    else:
        num4 += str(n % 3)
    r = int(num4, 4)
    if r <= 340:
        b.append(r)

print(max(b))
