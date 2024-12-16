def decimalToAny(num, base):
    numBase = ''
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while num > 0:
        numBase = alphabet[num % base] + numBase
        num //= base
    return numBase


def sumDigitsInString(string):
    sumDigits = 0
    for digit in string:
        sumDigits += int(digit)
    return sumDigits

sasha = '1234567'
print(sasha[:2])

ans = []
for n in range(1000000, 10000000):
    n_3 = decimalToAny(n, 3)
    if len(n_3) % 2 == 1:
        n_3 = '1' + n_3
    sumDigits = sumDigitsInString(n_3)
    if sumDigits % 2 == 0:
        n_3 += n_3[0:2]
    else:
        n_3 += decimalToAny(n % 5, 3)

    if n_3[0] == '2':
        n_3 = str(int(n_3[1:]))

    if n_3[-1] == n_3[-2]:
        n_3 = n_3[:-1]

    r = int(n_3, 3)

    if r > 150:
        ans.append(r)

print(min(ans))