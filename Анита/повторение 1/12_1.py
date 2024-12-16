def sumDigitsInString(string):
    sumDigits = 0
    for digit in string:
        sumDigits += int(digit)
    return sumDigits


for n in range(11, 10000):
    s = '3' + n * '5'

    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25', '32', 1)
        s = s.replace('355', '25', 1)
        s = s.replace('555', '3', 1)

    if sumDigitsInString(s) % 25 == 0:
        print(n)
        break