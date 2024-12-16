f = open('9 (6).txt').readlines()
ans = 0
for i in f:
    a = list(map(int, i.split()))
    b = set(a)
    if len(b) < len(a):
        flag = False
        nepovtor = []
        povtor = []
        for num in b:
            if a.count(num) == 2:
                flag = True
                povtor.append(num)
            if a.count(num) == 1:
                nepovtor.append(num)

        flag2 = True
        for pov in povtor:
            for nepov in nepovtor:
                if pov <= nepov:
                    flag2 = False
        if flag and flag2:
            ans += 1
print(ans)



