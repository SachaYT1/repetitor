f = open('9_2.txt').readlines()
count = 0
for s in f:
    a = list(map(int, s.split()))
    b = set(a)
    if len(b) == 4:
        flag = True
        sum_povtor = 0
        multiply_nepovtor = 1
        for j in b:
            if a.count(j) == 3:
                sum_povtor = j * 3
            elif a.count(j) == 2:
                flag = False
                break
            elif a.count(j) == 1:
                multiply_nepovtor *= j

        if flag:
            if multiply_nepovtor > sum_povtor:
                count += 1
print(count)