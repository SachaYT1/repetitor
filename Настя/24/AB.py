f = open('AB.txt').read()

m = 0
c = 0

f = f.replace('AB', 'A B')
a = f.split()

for i in range(101):
    c += len(a[i])
m = c

for i in range(101, len(a)):
    c += len(a[i])
    c -= len(a[i - 101])
    if c > m:
        m = c
print(m)