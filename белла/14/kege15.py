def perevod(num, base):
    num_base = ''
    while (num > 0):
        num_base = str(num % base) + num_base
        num //= base
    return num_base


for x in range(21, 30):
    if perevod(x, 3)[-2] + perevod(x, 3)[-1] == '11':
        print(x)