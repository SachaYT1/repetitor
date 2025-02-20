def deliteli(num):
    ans = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans


for num in range(608_006_8, 608_017_6 + 1):
    delit = deliteli(num)
    if len(delit) == 0:
        print(num)