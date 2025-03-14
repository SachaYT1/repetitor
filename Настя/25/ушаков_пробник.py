def deliteli(num):
    a = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            a.add(i)
            a.add(num // i)
    return a


def f(num):
    delit = deliteli(num)
    summa = 0
    for d in delit:
        if len(deliteli(d)) == 2:
            summa += d
    return summa

for i in range(1, 10**6):
    numF = f(i)
    if numF % 24453 == 0:
        print(i, numF)

