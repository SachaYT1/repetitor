from itertools import product
a = product('0123456789ABC', repeat=7)

chet = '02468AC'
nechet = '13579B'

c = 0
for i in a:
    s = ''.join(i)
    if s[0] != '0':
        if s.count('5') >= 2:
            flag = True
            for digit in range(0, len(s) - 1):
                if (s[digit] in chet and s[digit + 1] in chet) or \
                        (s[digit] in nechet and s[digit + 1] in nechet):
                    flag = False
                    break
            if flag:
                c += 1
print(c)