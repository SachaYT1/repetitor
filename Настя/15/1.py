for A in range(0, 300):
    flag = True
    for x in range(1, 301):
        for y in range(1, 301):
            f = (x >= A) or (y >= A) or (x * y <= 205)
            if not f:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
