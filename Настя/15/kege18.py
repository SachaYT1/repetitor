min_len = 10**9
for a in range(1, 500):
    for b in range(a, 500):
        flag = True
        for i in range(2, 500):
            x = i / 2
            f = not((72 <= x <= 106) and
                     not (a <= x <= b)) or (
                        not (not (64 <= x <= 95)) or not (
                        72 <= x <= 106
                    )
                )
            if not f:
                flag = False
                break
        if flag:
            min_len = min(min_len, b - a)
print(min_len)
