def deliteli(num):
    ans = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans

for num in range(25_317, 51_237 + 1):
    delit = deliteli(num)
    count = 0
    primes = []
    for x in delit:
        if len(deliteli(x)) == 0:
            count += 1
            primes.append(x)
    if count >= 6:
        print(num, max(primes))

