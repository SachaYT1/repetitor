from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 42:
        return 42
    if n > 42:
        return (n + 1) * (n - 1) * f(n - 1)


for i in range(42, 2050):
    f(i)

print((f(2042) + f(2043)) / f(2041))


