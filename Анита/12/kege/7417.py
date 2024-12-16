from math import sqrt


def isNumPrime(num):
    flag = True
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            flag = False
            break
    return flag


for n in range(0, 100):
    sumDigitsInString = 37 * 1 + 37 * 2
    sumDigitsInString += n * 4
    if isNumPrime(sumDigitsInString):
        print(n)
        break
