f = open('9.txt').readlines()
count = 0
for i in f:
    a = list(map(int, i.split()))
    b = set(a)
    if len(b) == 4:
        flag = True
        sum_nepovtor = 0
        povtor = 0
        for num in b:
            if a.count(num) == 3:
                povtor = num
            if a.count(num) == 2:
                flag = False
            if a.count(num) == 1:
                sum_nepovtor = sum_nepovtor + num
        if flag:
            if (povtor * 3) ** 2 > sum_nepovtor ** 2:
                count += 1
print(count)
