f = open('KEGE_4.txt').read()

c = 0
cMax = 0
for i in range(0, len(f) - 1):
    if (f[i] == 'X' and f[i + 1] == 'Y') \
        or (f[i] + f[i + 1] == 'XZ'):
        c += 1
        cMax = max(cMax, c)
        c = 0
    else:
        c += 1
        cMax = max(c, cMax)
 
print(cMax)