def deliteli(num):
    a = set()
    for x in range(2, round(num ** 0.5) + 1):
        if num % x == 0:
            a.add(x)
            a.add(num // x)
    return a

def P(n):
    d = deliteli(n)
    if len(d) >= 5:
        s = list(d)
        s.sort()
        p = 1
        for i in range(5):
            p *= s[i]
        return p, s[4]
    else:
        return 0, 0
    

k = 0    
for x in range(400_000_000, 10**9):
    p, maxDelit = P(x)
    if p % 100 == 17 and p <= x:
        print(p, maxDelit)
        k += 1
        if k == 5:
            break


    

