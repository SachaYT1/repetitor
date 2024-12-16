f = open('24 (1).txt').read().strip()

ans = -1

c = 0
f = '7' + f
for i in range(len(f)):
    if f[i] in 'SQRP':
        if f[i - 1] + f[i] in 'PSQRP':
            c += 1
        else:
            c = 1
    else:
        c = 0
    ans = max(ans, c)
print(ans)