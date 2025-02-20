def f(s1, s2, c, m):
    if s1 >= 40 or s2 >= 40:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = []
    if s1 > s2:
        h += [f(s1 + 1, s2, c + 1, m ),
                 f(s1 + 2, s2, c + 1, m ),
                 f(s1 + 3, s2, c + 1, m )]
        h += [f(s1, s2 * 2, c + 1, m)]
    elif s2 > s1:
        h += [f(s1, s2 + 1, c + 1, m ),
                 f(s1, s2 + 2, c + 1, m ),
                 f(s1, s2 + 3, c + 1, m )]
        h += [f(s1 * 2, s2, c + 1, m)]
    else:
        h += [f(s1 + 1, s2, c + 1, m ),
                 f(s1 + 2, s2, c + 1, m ),
                 f(s1 + 3, s2, c + 1, m )]
        h += [f(s1, s2 + 1, c + 1, m ),
                 f(s1, s2 + 2, c + 1, m ),
                 f(s1, s2 + 3, c + 1, m )]
 
    return any(h) if c % 2 != m % 2 else all(h)

a = []

for s2 in range(1, 40):
    for m in range(5):
        if f(31, s2, 0, m):
            if m == 4:
                print(s2)
            break

            