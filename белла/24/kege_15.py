f = open('KEGE_15.txt').read()



f = f.replace('BB', '*').replace('*B', '* *')
f = f.replace('DD', '?').replace('?D', '? ?')

f = f.replace('A', ' ').replace('B', ' ').replace('D', ' ')


a = f.split()
m = 0
for i in a:
    m = max(len(i), m)
print(m)