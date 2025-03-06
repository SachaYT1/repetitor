f = open('KEGE_10.txt').read()


f = f.replace('O', 'N').replace('P', 'N')
while 'NN' in f: f = f.replace('NN', 'N N')

a = f.split()

m = 0
for i in a:
    m = max(len(i), m)
print(m)