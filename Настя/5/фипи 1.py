def sumInString(string):
    a = 0
    for digit in string:
        a += int(digit)
    return a


def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base


for n in range(2, 10000):
    n_2 = bin(n)[2:]
    if n_2.count('1') % 2 == 0:
        n_2 = '10' + n_2[2:] + '0'
    else:
        n_2 = '11' + n_2[2:] + '1'
    r = int(n_2, 2)
    if r > 40:
        print(n)
        break
