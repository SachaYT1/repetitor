from sys import setrecursionlimit
setrecursionlimit(2100)


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (2 * n - 2) * f(n - 1)


print(f(2012) / f(2010))