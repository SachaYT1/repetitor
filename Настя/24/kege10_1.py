f = open('24_8510.txt').read()

f = f.replace('O', 'N').replace('P', 'N')

while 'NN' in f: f = f.replace('NN', 'N N')


m = 0
s = f.split()
for string in s:
    m = max(m, len(string))
print(m)