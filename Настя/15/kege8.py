for a in range(1, 3000):
    flag = True
    for x in range(1, 3000):
        f = not(x & 107 == 0) or (not(x & 55 != 0) or (x & a != 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)
