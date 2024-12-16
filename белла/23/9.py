def f(x, y, c):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y, c + (1 - (x + 1) % 2)) + f(x * 2, y,  c + (1 - (x * 2 ) % 2)) + f(x * 3, y)

ans = 0
for x in range(2, 14 + 1, 2):
    ans += f(x, 15)

print(ans)