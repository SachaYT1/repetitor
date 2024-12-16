f = open('24 (1).txt').read()

f = f.replace('SQRP', '*')


f = f.replace('S', ' ').replace('Q', ' ').replace('R', ' ').replace('P', ' ')
c = 0
c_max = 0
indx_pred = 0
posled = ''
max_posled = ''
for i in range(1, len(f)):
    if f[i] == '*':
        c += 4
        posled += 'SQPR'
        c += min(3, i - indx_pred - 1)
        posled += f[i - indx_pred - 1:i]
        if c > c_max:
            c_max = c
            max_posled = posled
        indx_pred = i
    else:
        for j in range(i + 1, min(i + 3 + 1, len(f))):
            if f[j] == '*':
                break
            else:
                c += 1
        c_max = max(c_max, c)
        c = 0
        posled = ''
print(c_max)

# print(max_posled)