def sumDigits(string):
    sum_digits = 0
    for elem in string:
        sum_digits += int(elem)
    return sum_digits


for n in range(3, 9999, 1):
    s = '5' + n * '2'
    while '52' in s or '2222' in s or '1122' in s:
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)


    if sumDigits(s) == 64 and n == 156:
        print(n)
        print(s, s.count('1'))


