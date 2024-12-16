min_len = 10 ** 9
for a in range(1, 500):
    for b in range(a, 500):
        flag = True
        for i in range(2, 1000):
            x = i / 3
            f = not (not (a <= x <= b) and
                     (74 <= x <= 194)) or (
                        not (74 <= x <= 194) or not (
                        152 <= x <= 223
                )
                )
            if not f:
                flag = False
                break
        if flag:
            min_len = min(min_len, b - a)
print(min_len)
