input_file = open('9 (5).txt').readlines()
ans = 0
for a in input_file:
    flag1 = False
    flag2 = False
    one = list(map(int, a.split()))
    sOne = set(one)
    if len(sOne) < 4:
        flag1 = True

    count_nechet = 0
    for num in one:
        if num % 2 != 0:
            count_nechet += 1
    if count_nechet == 3:
        flag2 = True

    if flag2 + flag1 == 1:
        ans += 1
print(ans)