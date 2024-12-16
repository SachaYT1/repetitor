f = open('9 (3).txt').readlines()
ans = 0
for i in f:
    a = list(map(int, i.split()))
    b = set(a)
    summa_chet = 0
    count_chet = 0
    summa_nechet = 0
    count_nechet = 0
    sr_arifm_chet = 0
    sr_arifm_nechet = 0
    for num in a:
        if num % 2 == 0:
            summa_chet += num
            count_chet += 1
        else:
            summa_nechet += num
            count_nechet += 1
    if count_chet == 0:
        sr_arifm_chet = 0
    elif count_nechet == 0:
        sr_arifm_nechet = 0
    else:
        sr_arifm_chet = summa_chet / count_chet
        sr_arifm_nechet = summa_nechet / count_nechet

    if (len(b) == 5) + (abs(sr_arifm_chet - sr_arifm_nechet) > 50) == 1:
        ans += 1
print(ans)
