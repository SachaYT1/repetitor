def f(x, y, count):
    if x > y:
        return 0
    if x == y and count == 6:
        return 1
    return f(x + 1, y,'C') + f(x + 3, y, count + x % 2) + f(x + 5, y, count + x % 2)
print(f(3, 25, 0))
