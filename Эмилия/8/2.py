from itertools import product, permutations

a = product('ABCWXYZ', repeat=6)

k = 0
for i in a:
    s = ''.join(i)
    if (s[0] in 'WXYZ' and s[5] in 'WXYZ'):
        if (s[1] not in 'WXYZ' and s[2] in 'ABC'  and s[3] in 'ABC'  and s[4] in 'ABC' ):
            k += 1
        

print(k)