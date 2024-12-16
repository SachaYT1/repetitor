

def f(s, c, m):
    if 65 <= s <= 100:
        return c % 2 == m % 2
    if s > 100:
        return c % 2 != m % 2

    if c == m:
        return 0

    h = [f(s + 1, c + 1, m), f(s * 3, c + 1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)

a = 'ОСОБА'
if a == 'ОСОБА':
    print(1)


for s in range(1, 64 + 1):
    for m in range(5):
        if f(s, 0, m):
            if m == 4:
                print(s, m)
            break