f = open('demo_2025_9.txt').readlines()
count = 0
for one in f:
    a = list(map(int, one.split()))
    b = set(a)
    if len(b) == 4:
        flag = True
        sum_povtor = 0
        sum_nepovtor = 0
        for num in b:
            if a.count(num) == 3:
                sum_povtor += num
            elif a.count(num) == 2:
                flag = False
                break
            else:
                sum_nepovtor += num
        if flag:
            if (sum_povtor * 3) ** 2 > sum_nepovtor ** 2:
                count += 1
print(count)