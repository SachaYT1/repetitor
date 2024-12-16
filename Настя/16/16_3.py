def f(n):
    if n == 1:
        return 2
    elif n > 1 and f(n - 1) < 7555444:
        return f(n - 1) + 6
    else:
        return f(n - 1) - 7555444


a = []
for i in range(1, 100):
    print(f(i))

print(7555442 % 6)