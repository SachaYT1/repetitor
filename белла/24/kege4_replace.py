f = open('KEGE_4.txt').read()

f = f.replace('XY', 'X Y').replace('XZ', 'X Z')
a = f.split(' ')
m = 0
for string in a:
    m = max(m, len(string))
print(m)