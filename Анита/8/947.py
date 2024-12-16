from itertools import product
a = product('ABCD', repeat=4)
count = 0

for i in a:
    s = ''.join(i)
    if s[0] <= s[1] <= s[2] <= s[3]:
        count += 1
        print(s)
print(count)