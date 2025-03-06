f = open('KEGE_9.txt').read()

f = f.replace('B', 'A').replace('2', '1')
f = f.replace('11A', '*').replace('1', ' ').replace('A', ' ')

a = f.split()

m = 0
for i in a:
    m = max(len(i), m)
print(m)