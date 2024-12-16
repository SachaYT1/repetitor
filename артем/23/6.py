def f(x, y, count):
    if x > y:
        return 0
    elif x == y and count <= 3:
        return 1
    return f(x + 2, y, count) + f(x * 3, y, count + 1) + f(x * 5, y, count + 1)

print(f(2, 200, 0))