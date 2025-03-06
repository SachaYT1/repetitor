f = open('KEGE_19.txt').read()

f = f.replace('T', ' ')
a = f.split(' ')


ans = 0
len_posled = 0

for i in range(101):
    len_posled += len(a[i])
len_posled += 100

ans = len_posled

for i in range(101, len(a)):
    len_posled += len(a[i])
    len_posled -= len(a[i - 101])
    if ans < len_posled:
        ans = len_posled
print(ans)
