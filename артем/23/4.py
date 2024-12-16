c = 0

def f(x, count):
    global c
    if count > 3:
        return 0
    if x % 2 == 0 and count > 0:
        c += 1
    return f(x + 1, count + 1) + f(x + 2, count + 1) + f(x * 3, count + 1)


print(f(4, 0))

print(c)
