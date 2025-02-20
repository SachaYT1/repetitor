from fnmatch import *

def deliteli(num):
    ans = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans


k = 0
for num in range(10**7, 90557, -1):
    if fnmatch(str(num), '9?*55*7'):
        print(num, sum(deliteli(num)) % 21)
        k += 1
        if k == 5:
            break