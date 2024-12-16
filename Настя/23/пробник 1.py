def f(x, count):
    if count == 4:
        return x
    return f(x + 2, count + 1) + f(x * 3, count + 1)

a = set()

print(f(1, 0))