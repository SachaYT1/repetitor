def perevod(num, base):
    num_base = ''
    alpabet = ['A', 'B', 'C', 'D']
    while num > 0:
        if num % base >= 10:
            num_base = alpabet[num % base - 10]
        else:
            num_base = str(num % base) + num_base
        num //= base
    return num_base

# print(perevod(6789543543, 11))
#
# numm3 = '000120'
# print(numm3[::-1])
# print(perevod(int(numm3, 3), 3))
# summa = 0
# for i in numm3:
#     summa += int(i)
# print(summa)


b = []
for n in range(1, 10000):
    num3 = perevod(n, 3)
    n3 = ''
    for l in num3:
        if l == '1':
            n3 += '2'
        elif l == '2':
            n3 += '0'
        elif l == '0':
            n3 += '1'
    n3 = perevod(int(n3, 3), 3)
    n3 = n3[::-1]
    summa = 0
    for i in n3:
        summa += int(i)
    n3 = n3 + perevod(summa, 3)
    if n3 != '':
        r = int(n3, 3)
        if r > 10 ** 4:
            b.append(r)
print(min(b))
