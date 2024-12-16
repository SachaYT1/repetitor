f = open('24_2422 (1).txt').read()
c = 1
c_max = 1
for i in range(1, len(f)):
    if f[i] >= f[i - 1]:
        c += 1
        if c > c_max:
            c_max = c
    else:
        c = 1
print(c_max)