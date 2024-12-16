for n in range(100, 1000):
    numStr = str(n)
    digit1 = int(numStr[0])
    digit2 = int(numStr[1])
    digit3 = int(numStr[2])
    ans = str(max(digit1 ** 2 + digit2 ** 2, digit2 ** 2 + digit3 ** 2)) \
          + str(min(digit1 ** 2 + digit2 ** 2, digit2 ** 2 + digit3 ** 2))
    if ans == '9010':
        print(n)
        break
