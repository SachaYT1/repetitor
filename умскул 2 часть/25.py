def eratosphenSieve(n):
    primes = [i for i in range(n + 1)]
    primes[1] = 0
    i = 2
    while i <= n:
        if primes[i] != 0:
            j = i + i
            while j <= n:
                primes[j] = 0
                j = j + i
        i += 1
    primes = [i for i in primes if i != 0]
    return primes

ans = []
for m in eratosphenSieve(10000):
    for n in range(2, 50, 2):
        num = 2 ** m * 5 ** n
        if 250_000_000 <= num <= 1_000_000_000:
            ans.append([num, bin(m ** 2 + n ** 2)[2:]])

ans.sort(key = lambda x: x[0])
for num, bins in ans:
    print(f'{num} {int(bins)}')
