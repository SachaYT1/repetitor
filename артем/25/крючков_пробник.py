def deliteli(num):
    a = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            a.add(i)
            a.add(num // i)
    return a

def f(num):
    delit = deliteli(num)
    F = 0
    for l in delit:
        if len(deliteli(l)) == 2:
            F += l
    return F


for i in range(1, 10 ** 6 + 1):
    numF = f(i)
    if numF % 24453 == 0:
        print(i, numF)
