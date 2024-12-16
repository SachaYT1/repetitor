from functools import lru_cache

@lru_cache(None)
def g(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 3) + f(n - 2)
    if n > 2 and n % 2 == 1:
        return f(n + 1) - g(n - 1)

@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 ==0:
        return g(n) + f(n - 1)
    if n > 2 and n % 2 ==1:
        return -2 * g(n + 1) + f(n - 2)


for i in range(1, 130):
    f(i)
    g(i)

print(g(120))