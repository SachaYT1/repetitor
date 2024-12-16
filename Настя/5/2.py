def sumDigitsInString(a):
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    return b

def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base


for n in range(1, 1001):
    n_2 = bin(n)[2:]
    n_2 = n_2[::-1]
    n_2 = n_2 + n_2[-1]
    r = int(n_2, 2)
    if r > 99:
        print(n)
        break



