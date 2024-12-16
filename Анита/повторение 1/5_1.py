from itertools import permutations
from math import sqrt


def isNumPrime(num):
    flag = True
    for j in range(2, round(sqrt(num)) + 1):
        if num % j == 0:
            flag = False
            break
    return flag


ans = []
countPrimeNumbersMax = -1
for n in range(100, 999 + 1):
    nString = str(n)
    countPrimeNumbers = 0
    a = permutations(nString, r=2)
    for i in a:
        numComb = "".join(i)
        if numComb[0] != '0':
            if isNumPrime(int(numComb)):
                countPrimeNumbers += 1

    ans.append([countPrimeNumbers, n])


ans.sort(key=lambda x: (-x[0], -x[1]))
print(ans)
print(ans[0][1])

