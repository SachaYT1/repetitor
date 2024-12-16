def decimalToAny(num, base):
    a = ''
    while num > 0:
        a = str(num % base) + a
        num //= base
    return a


def sumDigitsInString(string):
    ans = 0
    for digit in string:
        ans += int(digit)
    return ans


ans = []
for n in range(1, 10000):
    n_2 = decimalToAny(n * 2, 2)
    n_2 += str(sumDigitsInString(n_2) % 2)
    n_2 += str(sumDigitsInString(n_2) % 2)
    r = int(n_2, 2)
    if r > 1017:
        ans.append(r)
print(min(ans))

