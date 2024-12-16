def f(x, y, cmd):
    if x > y or x == 35:
        return 0
    if x == y and cmd == 'B':
        return 1
    return f(x + 1, y, 'A') + f(x + 2, y, 'B') + f(x + 4, y, 'C')


print(f(24, 33, '') * f(33, 42, ''))