def f(x: str, y: str):
    if int(x, 2) > int(y, 2):
        return 0
    if x == y:
        return 1
    return f(x + '0', y) + f(x + '1', y) + f(bin(int(x, 2) + 1)[2:], y)


print(f('100', '11101'))
       