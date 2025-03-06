f = open('KEGE_16.txt').read()

f = f.replace('PCSGO', '** ****')
f = f.replace('PC', '**').replace('CSGO', '****')

for i in range(ord('A'), ord('Z') + 1):
    f = f.replace(chr(i), ' ')

a = f.split()
m = 0
for i in a:
    m = max(len(i), m)
print(m)