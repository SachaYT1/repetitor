from fnmatch import *

for num in range(0, 10 ** 8, 141):
    if fnmatch(str(num), '1234*7'):
        print(num, num // 141)