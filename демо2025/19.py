def f(s, c, m):
    if s <= 19:
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(s - 2, c + 1, m), f(s - 5, c + 1, m), f(s // 3, c + 1, m)]
    return all(h) if (c + 1) % 2 == (m + 1) % 2 else any(h)

for s in range(20, 200):
    for m in range(5):
        if f(s, 0, m):
            if m == 4:
                print(s, m)
            break