f = open('24_13715.txt').read()

f = f.replace('AB', '*')
c = f.split('*')

ans = 0
len_posled = 0
k = 0
for i in range(0, 51):
    len_posled += len(c[i])
    k += 1
len_posled += 50 * 2
ans = len_posled
for i in range(51, len(c)):
    len_posled += len(c[i])
    len_posled -= len(c[i - 51])
    ans = max(ans, len_posled)
print(ans)