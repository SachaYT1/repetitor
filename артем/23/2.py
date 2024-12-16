def f(x, y, com):
    if x > y:
        return 0
    if x == y and (com == 'A' or com == 'B'):
        return 1
    return f(x + 2, y, 'A') + f(x + 5, y, 'B') + f(x * 2, y, 'C')

print(f(8, 40, ''))