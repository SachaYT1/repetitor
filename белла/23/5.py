def f(x, y, c):
    if x > y or x == 27:
        return 0
    if x == y and (c <= 15):
        return 1

    return f(x + 2, y, c + 1) + f(x * 3, y, c + 1) + f(x ** 3, y, c + 1)

print(f(3, 125, 0))

