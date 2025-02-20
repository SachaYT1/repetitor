def deliteli(num):
    ans = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans 

k = 0
for num in range(550_000 + 1, 10**6):
    delit = deliteli(num)
    if len(delit) != 0:
        f = sum(delit) // len(delit)
        if f % 31 == 13:
            print(num, f)
            k += 1
            if k == 5:
                break