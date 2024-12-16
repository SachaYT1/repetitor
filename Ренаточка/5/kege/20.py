def multiplyDigits(n, m):
    evenDigits = []
    oddDigits = []
    for digit in str(n):
        if int(digit) % 2 == 0:
            evenDigits.append(int(digit))
        else:
            oddDigits.append(int(digit))
    for digit in str(m):
        if int(digit) % 2 == 0:
            evenDigits.append(int(digit))
        else:
            oddDigits.append(int(digit))
    p1 = 1
    p2 = 1
    for i in evenDigits:
        if i != 0:
            p1 *= i
    for i in oddDigits:
        if i != 0:
            p2 *= i
    return abs(p1 - p2)


for m in range(0, 20000):
    if multiplyDigits(m, 120) == 29:
        print(m)
        break

