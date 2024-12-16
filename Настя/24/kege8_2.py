f = open('24_4602.txt').read()

soglas = ['B', 'C', 'D']
glas = ['A', 'O']

c_max = 0
c = 0
for i in range(1, len(f), 2):
    if f[i - 1] in soglas and f[i] in glas:
        c += 1
        if c > c_max:
            c_max = c
    else:
        c = 0

c = 0
for i in range(2, len(f), 2):
    if f[i - 1] in soglas and f[i] in glas:
        c += 1
        if c > c_max:
            c_max = c
    else:
        c = 0

print(c_max)