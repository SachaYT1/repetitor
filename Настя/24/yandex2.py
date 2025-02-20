

f = 'GFRREAAAAGREGARGA'
f = f.replace('A', ' ')
f = f.split(' ')

ans = 0
len_posled = 0
for i in range(0, 241):
    len_posled += len(f[i])
    if len_posled > ans:
        ans = len_posled
len_posled += 240
ans = len_posled
for i in range(241, len(f)):
    len_posled += len(f[i])
    len_posled -= len(f[i - 241])
    ans = max(ans, len_posled)
print(ans)