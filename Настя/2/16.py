from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(5000)

@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 100 == 0:
        return f(n - 1) * f(n -2) + f(1)
    if n > 1 and n % 100 != 0:
        return n * f(n - 1)

print(f(2042))