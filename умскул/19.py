def f(s1, s2, c, m):
    if s1 * s2 >= 222:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(s1 + 3, s2, c + 1, m), f(s1 + 6, s2, c + 1, m), f(s1, s2 + 3, c + 1, m), f(s1, s2 + 6, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s2 in range(1, 27 + 1):
    for m in range(5):
        if f(8, s2, 0, m):
            if m == 4:
                print(s2, m)
            break