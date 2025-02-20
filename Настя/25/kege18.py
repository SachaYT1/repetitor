def deliteli(num):
    delit = set()
    count_nechet = 0
    flag = False
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            if i % 2 == 1:
                delit.add(i)
                count_nechet += 1
            if (num // i) % 2 == 1:
                delit.add(num // i)
                count_nechet += 1
        if count_nechet > 5:
            flag = False
            break
    if count_nechet == 5:
        flag = True
    return delit, flag

print((55383364 ** 0.5) ** 0.5)

for num in range(55_000_000, 60_000_000 + 1):
    delit, flag = deliteli(num)

    if flag:
        print(num, max(delit))
    