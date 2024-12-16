f = open('24 (3).txt').readline()
f = f.replace('XYZY', '_YZY')
c = 0
cMax = 0
i = 0
while i < len(f) - 1:
    if (f[i] == 'X' or f[i] == 'Z') and f[i + 1] == 'Y':
        c += 1
        cMax = max(cMax, c)
        i += 2
    else:
        c = 0
        i += 1
print(cMax)

