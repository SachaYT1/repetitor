f = open('24_8510.txt').read()

f = f.replace('O', 'N').replace('P', 'N')
while 'NN' in f:
    f = f.replace('NN', 'N N')

ans = 0
s = f.split()

for string in s:
    ans = max(ans, len(string))
print(ans)