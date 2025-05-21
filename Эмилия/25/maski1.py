from fnmatch import *

# или 0 
for num in range(1021394 - 1021394 % 2023, 10**10, 2023):
    if fnmatch(str(num), '1?2139*4'):
        print(num, num // 2023)