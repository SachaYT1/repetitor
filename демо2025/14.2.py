def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base

a = []
for x in range(1, 2030 + 1):
    num = 7 ** 170 + 7 ** 100 - x
    num_7 = perevod(num, 7)
    if num_7.count('0') == 71:
        a.append(x)
print(max(a))
