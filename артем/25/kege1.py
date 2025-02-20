def deliteli(num):
    ans = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans

for num in range(174457, 174505 + 1):
    delit = deliteli(num)
    if len(delit) == 2:
        a = list(delit)
        a.sort()
        for num2 in a:
            print(num2, end=' ')
        print()