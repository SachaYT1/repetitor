def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base


s = []
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '1' + n2 + '0'
    else:
        n2 = '11' + n2 + '11'
    
    r = int(n2, 2)
    if r > 52:
        s.append(r)
print(min(s))