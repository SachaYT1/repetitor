f = open('KEGE_14.txt').read()
c_max = 1
c = 1
posledMax = f[0]
posled = f[0]

# ord()
# chr()

for i in range(1, len(f)):
    if f[i] < f[i - 1]:
        posled += f[i]
        c += 1
        if c > c_max:
            c_max = c
            posledMax = posled
    else:
        c = 1
        posled = f[i]

print(posledMax)
