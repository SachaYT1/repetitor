from functools import *
from math import trunc, ceil
@lru_cache(None)

def f(n):
    if n <= 18:
        return n + 3
    if n > 18 and n % 3 == 0:
        return (n // 3) * f(n//3) + n - 12
    if n > 18 and n % 3 != 0:
        return f(n - 1) + n ** 2 + 5


def check(num: int):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True


count = 0
for n in range(1, 1001):
    num = f(n)
    if check(num):
        count += 1
print(count)
