def f(x, y, cmd):
    if x > y:
        return 0
    if x == y and (cmd == 'A' or cmd == 'B'):
        return 1

    return f(x + 2, y, 'A') + f(x + 5, y, 'B') + f(x * 2, y, 'C')
#
# print(f(8, 38) + f(8, 35))
print(f(8, 40, ''))

