from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(3000)
@lru_cache(None)
def f(n):
    if n > 3000:
        return n
    else:
        return (2 * n + 4) * f(n + 2)


for i in range(3000, 19, -1):
    f(i)
num = int(f(20) / f(28))
print(num)

sumOfDigits = 0
for digit in str(num):
    sumOfDigits += int(digit)
print(sumOfDigits)