def deliteli(num):
    delit = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            delit.add(i)
            delit.add(num // i)
    return delit

for i in range(10332, 12356 + 1):
    num = i ** 2
    delit = deliteli(num)
    if len(delit) == 3:
        print(num, max(delit))