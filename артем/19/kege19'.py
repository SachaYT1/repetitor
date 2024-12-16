count = set()
def f(s, c, m):
    global count
    if 5 <= s <= 25:
        count.add(s)
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(s + 1, c + 1, m),f(s + 2, c + 1, m),
         f(s + 3, c + 1, m), f(s + 4, c + 1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)


s1 = 0
for m in range(5):
    if f(s1, 0, m):
        if m == 3:
            print(s1, m)

print(len(count))