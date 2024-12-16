def decimalToAny(num, base):
    num_base = ''
    while (num > 0):
        num_base = str(num % base) + num_base
        num //= base
    return num_base


ans = []
for n in range(2 ** 6, 2 ** 9 + 1):
    n_3 = decimalToAny(n, 3)
    n_3 += n_3[0]
    n_3 += str((n_3.count('1') + n_3.count('2') * 2) % 2)
    n_3 = n_3[::-1]
    r = int(n_3, 3)
    if r > 400:
        ans.append([r, n])

ans.sort()
print(ans)

