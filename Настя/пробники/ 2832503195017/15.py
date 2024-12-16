def digit(num, d):
    if (num % 10) == (d % 10):
        return True
    else:
        return False


for a in range(1000, 1, -1):
    flag = True
    for x in range(1, 1000):
        f = not(not(digit(x, 5)) and digit(x, 4)) or (x > a - 11)
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break
