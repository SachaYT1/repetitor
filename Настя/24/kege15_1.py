f = open('24_4113.txt').read()


c_max = 0
c1 = 0
ans = ''
for i in range(1, len(f), 2):
    if (f[i - 1] + f[i]) in ['BB', 'DD']:
        c1 += 1
        if c1 > c_max:
            c_max = c1
    else:
        c1 = 0

c_max = 0
c1 = 0
for i in range(2, len(f), 2):
    if (f[i - 1] + f[i]) in ['BB', 'DD']:
        c1 += 1
        if c1 > c_max:
            c_max = c1
    else:
        c1 = 0



print(c_max)