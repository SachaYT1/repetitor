f = open('9_1.txt').readlines()

for i in f:
    a = list(map(int, i.split()))
    b = set(a)

    if len(b) == 4:
        flag = True
        for j in b:
            if a.count(j) != 3 and a.count(j) != 1:
                flag = False
                break

        if a.count(min(a)) != 1:
            flag = False

        if flag:
            summ = sum(a)
            print(summ)
            break


