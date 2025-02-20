for a in range (1, 500):
    flag = True
    for x in range(1, 500):
        f = not((x & 26 != 0) or (x & 13 != 0)) or (not(x & 29 == 0) or (x & a != 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break