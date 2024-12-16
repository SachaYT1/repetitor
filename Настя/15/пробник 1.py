for a in range(1, 300):
    flag = True
    for b in range(a, 300):
        for x in range(1, 400):
            f = not ((72 <= x <= 106) and
                     not (a <= x <= b)) or (
                        not (not (64 <= x <= 95)) or not (
                        72 <= x <= 106
                    )
                )
            if not f:
                flag = False
                break
        if not flag:
            break
    if flag:



