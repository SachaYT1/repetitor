def f(s1, s2, c, m):
    if s1 + s2 >= 131:
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(s1 + 2, s2, c + 1, m), f(s1 * 2, s2, c + 1, m),
         f(s1, s2 + 2, c + 1, m), f(s1, s2 * 2, c + 1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s2 in range(1, 119 + 1):
    for m in range(5):
        if f(11, s2, 0, m):
            if m == 4:
                print(s2, m)
            break