def decimalToAny(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base if num_base != '' else '0'

ans = []
for elem in range(0, 10000):
    num_2 = decimalToAny(elem, 2)
    if num_2.count('1') % 2 == 0:
        num_2 += '0'
    else:
        num_2 += '1'
    if num_2.count('1') % 2 == 0:
        num_2 += '0'
    else:
        num_2 += '1'
    r = int(num_2, 2)
    if r > 96:
        ans.append(r)
print(min(ans))

