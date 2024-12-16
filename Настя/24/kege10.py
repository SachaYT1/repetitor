f = open('24_8510.txt').read()

f = f.replace('O', 'N').replace('P', 'N')


c_max = 0

c = 1
for i in range(1, len(f)):
    if not(f[i - 1] == 'N' and f[i] == 'N'):
        c += 1
        c_max = max(c_max, c)
    else:
        c = 1

print(c_max)