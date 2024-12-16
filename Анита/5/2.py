for x in range(99, 9, -1):
    y = ''
    y_str = str(x % 4) + str(x % 3) + str(x % 2)
    y_int = (x % 4) * 100 + (x % 3) * 10 + (x % 2)
    if y_str == '101' or y_int == 101:
        print(x)
        break
