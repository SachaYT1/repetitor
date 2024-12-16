from itertools import product
a = product('АГИЛМОРТ', repeat=4)
ans = []
number = 1
s = '12345'
for i in a:
    s = ''.join(i)
    if s[-2:] == 'ИМ':
        ans.append(number)
    number += 1
print(max(ans))
