def deliteli(num):
    ans = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans
k = 0
for num in range(400_000_001, 10**9):
    delit = deliteli(num)
    if len(delit) >= 5:
        a = list(delit)
        a.sort()
        p = 1
        for i in range(5):
            p *= a[i]
        if p % 100 == 17 and p <= num:
            print(p, a[4])
            k += 1
            if k == 5:
                break