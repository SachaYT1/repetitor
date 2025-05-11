def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base

a = '5743865298'
b = '567'
# '567567567'
# '5', '6', '7'

def sumInString(num: str):
    summa = 0
    for digit in num:
        summa += int(digit)
    return summa

print(sumInString('123'))

print(sumInString(a))


s = []
for n in range(2, 1000):
    n2 = bin(n)[2:]
    if sumInString(n2) % 2 == 0:
        n2 = '10' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'
    
    r = int(n2, 2)
    if r < 35:
        s.append(n)
print(max(s))