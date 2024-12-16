from sys import setrecursionlimit
setrecursionlimit(2500)
def f(n):
    if n == 1:
        return n
    elif n > 1:
        return (5 * n + 3) + f(n - 1)

print(f(2022) / f(2019))