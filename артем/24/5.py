f = open('5.txt').read()

soglas = 'KLMN'
glas = 'AEOU'
c = 1
ans = 1
for i in range(1, len(f)):
    if (f[i] in soglas and f[i - 1] in glas) or \
    (f[i] in glas and f[i - 1] in soglas):
        c += 1
        ans = max(ans, c)
    else:
        c = 1
print(ans)
    