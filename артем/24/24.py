f = open('24.txt').read()

f = f.replace('FAT', '*').replace('BAD', '*')

a = f.split('*')


m = 0
c = 9

for i in range(0, 2):
    c += len(a[i])

m = c 

for i in range(2, len(a)):
    c += len(a[i])
    c -= len(a[i - 2])
    m = min(m, c)

print(m)