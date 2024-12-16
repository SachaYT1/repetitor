f = open('9.txt').readlines()
count = 0
for i in f:
    a = list(map(int, i.split()))
    b = set(a)
    if len(b) == 4:
        povtor_num = 0
        sum_nepovtor = 0
        flag = False
        for num in b:
            if a.count(num) == 3:
                povtor_num = num
                flag = True
            elif a.count(num) == 2:
                flag = False
                break
            else:
                sum_nepovtor += num

        if flag:
            if (povtor_num * 3) ** 2 > sum_nepovtor ** 2:
                count += 1
print(count)