def deliteli(num):
    ans = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans

for num in range(154_026, 154_043 + 1):
    if len(deliteli(num)) == 4:
        delit = list(deliteli(num))
        delit.sort()
        print(delit[-2], delit[-1])