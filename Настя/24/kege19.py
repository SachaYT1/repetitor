f = open('24_10105.txt').read()

f = f.replace('T', ' ')
c = f.split(' ')

ans = 0
len_posled = 0
for i in range(0, 101):
    len_posled += len(c[i])
len_posled += 100
ans = len_posled
for i in range(101, len(c)):
    len_posled += len(c[i])
    len_posled -= len(c[i - 101])
    ans = max(ans, len_posled)
print(ans)
