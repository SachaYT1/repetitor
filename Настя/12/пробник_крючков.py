def sumInString(string):
    summa = 0
    for digit in string:
        summa += int(digit)
    return summa

s = '123' * 99
n = 0
flag = True

while (flag):
    n += 1
    s = s.replace('10', '', 1)
    s = s.replace('51', '4', 1)
    s = s.replace('23', '5', 1)
    s = s.replace('45', '', 1)
    if sumInString(s) <= 300:
        print(n)
        break
