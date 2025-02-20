for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            f = (x * y > a) and (x > y) and (x < 8)
            if f:
                flag = False
                break
        if not flag:
            break

    if flag:
        print(a)
        break