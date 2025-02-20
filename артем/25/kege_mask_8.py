from fnmatch import *

def deliteli(num):
    ans = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans


k = 0
for num in range(0, 10 ** 9, 168):
    if fnmatch(str(num), '?6*6*?6'):
        print(num, sum(deliteli(num)))
        k += 1
        if k == 7:
            break