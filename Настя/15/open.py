
for a in range(0, 3000):
    flag = True
    for x in range(0, 3000):
        f = not((x & 52 != 0) and (x & 48 == 0)) or not(x & a == 0)
        if f == 0:
            flag = False
            break
    if flag:
        print(a)
        break



