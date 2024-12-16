def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return base

num_2 = bin(123)[2:]
r = int(num_2, 2)