def decimalToAny(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    if num_base == '':
        return '0'
    return num_base

for n in range(0, 128):
    n_2 = decimalToAny(n, 2)
    n_2 = '0' * (8 - len(n_2)) + n_2
    n_2_inverted = ''
    for elem in n_2:
        if elem == '0':
            n_2_inverted += '1'
        else:
            n_2_inverted += '0'

    n_2_inverted = decimalToAny(int(n_2_inverted, 2) + 1, 2)
    r = int(n_2_inverted, 2)
    if n == 95:
        print(r)
