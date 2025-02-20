def deliteli(num):
    ans = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans


for num in range(190_201, 190_260):
    delit = deliteli(num)
    count_chet = 0
    chet_delit = []
    for l in delit:
        if l % 2 == 0:
            count_chet += 1
            chet_delit.append(l)
    
    if count_chet == 4:
        chet_delit.sort()
        print(chet_delit[-1], chet_delit[-2])