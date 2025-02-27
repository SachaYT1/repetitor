f= open('KEGE_5.txt').read()
while 'PP' in f:
    f = f.replace('PP', 'P P')


a = f.split(' ')
m = 0
for string in a:
    m = max(m, len(string))
print(m)