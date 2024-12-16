def f(x, y):
    if x > y or x == 23:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 3, y) + f(x * 4, y)

print(f(4, 18) * f(18, 35))