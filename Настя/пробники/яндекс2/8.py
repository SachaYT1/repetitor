from itertools import product, permutations

a = product('0123456789AB', repeat=7)

delit3 = ['0', '3', '6', '9']


count = 0
for j in a:
    s = ''.join(j)
    if s[0] != '0':
        flag = True
        for i in range(1, len(s)):
            if (s[i] in delit3 and s[i - 1] not in delit3) or \
                    (s[i] not in delit3 and s[i - 1] in delit3):
                pass
            else:
                flag = False
                break
        if flag:
            count += 1
print(count)


