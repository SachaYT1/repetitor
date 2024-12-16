def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)

ans = 0
for x in range(2, 14 + 1, 2):
    ans += f(x, 15)

print(ans)