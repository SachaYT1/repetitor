def decimalToAny(num, base):
    num_base = ''
    while (num > 0):
        num_base = str(num % base) + num_base
        num //= base
    return num_base

ans = []
for n in range(2 ** 6, 2 ** 9 + 1):
    num_3 = decimalToAny(n, 3)
    num_3 += num_3[-1]
    num_3 = num_3 + str((num_3.count('1') + num_3.count('2') * 2) % 2)
    num_3 = num_3[::-1]
    if int(num_3, 3) > 350:
        ans.append(int(num_3, 3))

print(min(ans))