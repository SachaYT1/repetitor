def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base


a = perevod(86, 8)
b = perevod(99, 8)
c = perevod(105, 8)

print(int('151', 8))

print(a, b, c)

