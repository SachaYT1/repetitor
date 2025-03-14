from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)

@lru_cache(None)
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 5, y, 'A') + f(x * 3, y, 'B') + f(x * 4, y, 'C')

# for i in range(23, 32323):
#     f(i, 32323)


print(f(23, 923))
print(f(923, 32323))