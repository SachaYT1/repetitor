f = open('KEGE 24 18285.txt').read()
f = f.replace('*', '+')
a = f.split('+')

c = 0
c_max = 0
for i in a:
    if i == '':
        c = 0
    elif i.startswith('0'):
        c = 0
    else:
        c += 1
        if c > c_max:
            c_max = c
print(c_max)

