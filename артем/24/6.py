f = open('6.txt').read()

c = 0
ans = 0
for i in range(2, len(f), 3):
    if (f[i - 2] + f[i - 1] + f[i]) == 'ABA' or \
    (f[i - 2] + f[i - 1] + f[i]) == 'BAB':
        c += 1
        ans = max(c, ans)
    else:
        c = 0

c = 0 
for i in range(3, len(f), 3):
    if (f[i - 2] + f[i - 1] + f[i]) == 'ABA' or \
    (f[i - 2] + f[i - 1] + f[i]) == 'BAB':
        c += 1
        ans = max(c, ans)
    else:
        c = 0

c = 0
for i in range(4, len(f), 3):
    if (f[i - 2] + f[i - 1] + f[i]) == 'ABA' or \
    (f[i - 2] + f[i - 1] + f[i]) == 'BAB':
        c += 1
        ans = max(c, ans)
    else:
        c = 0
print(ans)