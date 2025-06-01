# тут либо маска либо на поиск делителей, в целом всё изи, главное обратите внимание на НЕТРИВИАЛЬНЫЕ делители (не 1 и не само число)

def deliteli(num):
    ans = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans


count = 0
for num in range(round(106732567 ** 0.5) + 1, round(152673836 ** 0.5)):
    delit = deliteli(num ** 2)
    if len(delit) == 3:
        print(num ** 2, max(delit))


from fnmatch import *

for num in range(0, 10 ** 8, 141):
    if fnmatch(str(num), '1234*7'):
        print(num, num // 141)