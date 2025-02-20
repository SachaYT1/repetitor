from fnmatch import *



for num in range(1235670 - 1235670 % 169, 10 ** 9, 169):
    if fnmatch(str(num), '123*567?'):
        print(num, num // 169)