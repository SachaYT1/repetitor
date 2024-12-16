from math import sqrt


def isNumPrime(num):
    flag = True
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            flag = False
            break
    return flag


for n in range(0, 100):
    sumDigitsInString = 9
    sumDigitsInString += n * 3 + n * 5
    if 100 <= sumDigitsInString <= 999 and isNumPrime(sumDigitsInString):
        print(n)
        break
