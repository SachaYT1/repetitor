f = open('24_1302.txt').read()
a = f.replace('XZZY', 'XZZ ZZY')
c = a.split()
ans = 0
b = 0
for string in c:
    ans = max(ans, len(string))

print(ans)