def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base


a = []
for x in range(2300, 0, -1):
    num = 7 ** 350 + 7 ** 150 - x
    num7 = perevod(num, 7)
    if num7.count('0') == 200:
        a.append(x)
        break

print(a)

    