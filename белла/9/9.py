f = open('9.txt').readlines()
n = 0
ans = 0
for i in f:
    n += 1
    a = list(map(int, i.split()))
    b = set(a)
    if len(b) == 5:
        flag = True
        count_chet = 0
        count_nechet = 0
        for num in b:
            if a.count(num) == 3:
                pass
            elif a.count(num) == 2:
                flag = False

            if num % 2 == 0:
                count_chet += a.count(num)
            else:
                count_nechet += a.count(num)
        if count_chet > count_nechet and flag:
            ans = n
print(ans)


