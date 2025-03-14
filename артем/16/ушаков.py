from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 10:
        return n ** 2
    elif n % 2 == 1 and n > 10:
        return f(n - 3) - f(n - 2) + f(n - 1)
    elif n % 2 == 0 and n > 10:
        return f(n // 2)


for i in range(1, 2026):
    f(i)

print(f(2025))