f = open('15.txt').read()

c = 0
m = 0
for i in range(1, len(f), 2):
    if f[i-1] + f[i] in ['BB', 'DD']:
        c += 1
        m = max(m, c)
    else:
        c = 0

c= 0
for i in range(2, len(f), 2):
    if f[i-1] + f[i] in ['BB', 'DD']:
        c += 1
        m = max(m, c)
    else:
        c = 0


print(m)