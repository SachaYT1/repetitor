f = open('24.txt').readline()


c1 = 0
c1Max =0

for i in range(0, len(f) - 1, 2):
    if f[i] + f[i + 1] == 'AA' or f[i] + f[i + 1] == 'CC':
        c1 += 1
        c1Max = max(c1, c1Max)
    else:
        c1 = 0

c2 = 0
c2Max = 0
for i in range(1, len(f) - 1, 2):
    if f[i] + f[i + 1] == 'AA' or f[i] + f[i + 1] == 'CC':
        c2 += 1
        c2Max = max(c2, c2Max)
    else:
        c2 = 0

print(max(c1Max, c2Max))

