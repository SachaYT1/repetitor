# перевод в троичную запись
def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base

for n in range(1, 1000):

    n_3 = perevod(n, 3)
