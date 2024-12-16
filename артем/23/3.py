
def f(x, y, count):
    if x > y or x == 27:
        return 0
    if x == y and count <= 15:
        return 1
    return f(x + 2, y, count+1) + f(x * 3, y, count+1) + f(x ** 3, y, count+1)

print(f(3, 125, 0))