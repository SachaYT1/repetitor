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