f = open('9 (2).txt').readlines()
ans = 0
for i in f:
    a = list(map(int, i.split()))
    c = 0
    summa_polozh = 0
    summa_otriz = 0
    for num in a:
        if num % 10 == 3:
            c += 1
        if num > 0:
            summa_polozh += num
        else:
            summa_otriz += num
    if c == 3 and summa_polozh ** 2 < summa_otriz ** 2:
        ans += 1
print(ans)
