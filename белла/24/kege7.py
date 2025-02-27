f = open('KEGE_7.txt').read()
c = 0 
cMax = 0
for i in range(0, len(f) - 2, 3):
    s = f[i] + f[i + 1] + f[i + 2]
    if s == 'NPO' or s == 'PNO':
        c += 1
        cMax = max(cMax, c)
    else:
        c = 0

c = 0
for i in range(1, len(f) - 2, 3):
    s = f[i] + f[i + 1] + f[i + 2]
    if s == 'NPO' or s == 'PNO':
        c += 1
        cMax = max(cMax, c)
    else:
        c = 0

c = 0
for i in range(2, len(f) - 2, 3):
    s = f[i] + f[i + 1] + f[i + 2]
    if s == 'NPO' or s == 'PNO':
        c += 1
        cMax = max(cMax, c)
    else:
        c = 0
print(cMax)