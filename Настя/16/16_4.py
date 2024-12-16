from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return 2 * f(1 - n) + 3 * f(n - 1) + 2
    if n < 0:
        return -f(-n)


for i in range(-100, 100):
    f(i)

print(f(50))
