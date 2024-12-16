from itertools import product

a = product('ABCDE', repeat=4)

ans = set()
for i in a:
    s = ''.join(i)
    if s[-1] in 'BCD' and s[1] in 'ABC' and s[0] != s[1]:
        if s[2] in 'BCD' and s[0] in 'AE':
            ans.add(s)
        elif s[2] in 'AE' and s[0] in 'BCD':
            ans.add(s)
print(len(ans))
