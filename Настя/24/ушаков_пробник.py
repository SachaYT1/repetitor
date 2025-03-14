f = open('KEGE 24.txt').read()


m = 1
c = 1
for i in range(1, len(f)):
    if f[i] >= f[i - 1]:
        c += 1
        m = max(c, m)
    else:
        c = 1
print(m)
