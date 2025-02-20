f = open('2.txt').read()
a = f.split('A')

ans = 0
len_posled = 0
for i in range(0, 241):
    len_posled += len(a[i])
len_posled += 240
ans = len_posled

for i in range(241, len(a)):
    len_posled += len(a[i])
    len_posled -= len(a[i - 241])
    ans = max(ans, len_posled)

print(ans)