f = open('KEGE_18.txt').read()

f = f.replace('D', ' ')
a = f.split(' ')

m = 0
for i in range(2, len(a)):
    len_posled = len(a[i - 2]) + len(a[i - 1]) + len(a[i]) + 2
    m = max(m, len_posled)
print(m)