from itertools import product
a = product('АКЛОШ', repeat=4)
number = 1
for i in a:
    s = "".join(i)
    if s[0] == 'О':
        print(number)
        break
    number += 1
