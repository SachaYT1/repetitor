from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(2000)
@lru_cache(None)
def f(n):
    if n == 41:
        return 41
    elif n > 41 and n % 2 == 0:
        return f(n - 1) - n
    elif n > 41 and n % 2 == 1:
        return n * f(n - 2)


for i in range(40, 9100):
    f(i)


print(f(9094) // f(9089))


