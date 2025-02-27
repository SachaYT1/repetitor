f = open('KEGE_7.txt').read()

f = f.replace('PNO', '*').replace('NPO', '*')
f = f.replace('P', ' ').replace('N', ' ').replace('O', ' ')
a = f.split()
m = 0
for string in a:
    m = max(m, len(string))
print(m)