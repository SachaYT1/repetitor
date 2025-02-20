from fnmatch import *



for num in range(123450600, 10 ** 9, 17):
    if fnmatch(str(num), '12345?6?8'):
        print(num, num // 17)


