from fnmatch import *

def deliteli(num):
    ans = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            if i % 2 == 1:
                ans.add(i)
            if (num // i) % 2 == 1:
                ans.add(num // i)
    return ans


k = 0
for num in range(10 ** 7 - (10 ** 7) % 217, 0, -217):
    if fnmatch(str(num), '14?4*'):
        print(num, sum(deliteli(num)))
        k += 1
        if k == 7:
            break


def sumRazrad(num):
    summa = 0
    for digit in str(num):
        summa += int(digit)
    return summa