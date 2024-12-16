from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
# @lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return f(n - 1) // 3
    if n > 1 and n % 2 == 1:
        return 6 * f(n - 1)

# for i in range(1, 2050):
#     f(i)

print(f(2049) / f(2046))
