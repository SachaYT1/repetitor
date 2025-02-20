min_len = 10**9
for l in range(1, 500):
    for r in range(l + 1, 500):
        flag = True
        for i in range(2, 500):
            x = i / 2
            f = not(17 <= x <= 58) or (not(not(29 <= x <= 80) and not(l <= x <= r)) or not(17 <= x <= 58))
            if not f:
                flag = False
                break
        if flag:
            min_len = min(min_len, r - l)

print(min_len)