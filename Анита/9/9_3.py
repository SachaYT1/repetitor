f = open('9 (4).txt').readlines()

for i in f:
    a = list(map(int, i.split()))
    b = set(a)
    if len(b) == 4:
        flag = True
        for j in b:
            if a.count(j) != 3:
                if a.count(j) != 1:
                    flag = False

        if a.count(min(a)) != 1:
            flag = False

        if flag:
            print(sum(a))
            break
