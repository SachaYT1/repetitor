def deliteli(num):
    delit = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            delit.add(i)
            delit.add(num // i)
    return delit


for num in range(125_697, 125_721 + 1):
    delit = deliteli(num)
    for i in delit:
        delit1 = i
        delit2 = num // i
        if len(deliteli(delit1)) == 0 and \
        len(deliteli(delit2)) == 0:
            print(min(delit1, delit2), max(delit1, delit2))
            break