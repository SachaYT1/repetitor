f = open('KEGE_17.txt').read()

c = 0
c_max = 0
for i in range(2, len(f), 3):
    if f[i - 2] + f[i] in ['AA', 'CC']:
        c += 1
        c_max = max(c, c_max)
    else:
        c = 0


c = 0
for i in range(3, len(f), 3):
    if f[i - 2] + f[i] in ['AA', 'CC']:
        c += 1
        c_max = max(c, c_max)
    else:
        c = 0

c = 0
for i in range(4, len(f), 3):
    if f[i - 2] + f[i] in ['AA', 'CC']:
        c += 1
        c_max = max(c, c_max)
    else:
        c = 0

print(c_max)