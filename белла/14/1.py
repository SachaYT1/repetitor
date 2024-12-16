def perevod(num, base):
    num_base = ''
    while (num > 0):
        num_base = str(num % base) + num_base
        num //= base
    return num_base


for x in range(1, 2030 + 1):
    num = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    num_6 = perevod(num, 6)
    if num_6.count('0') == 202:
        print(x)
        break
