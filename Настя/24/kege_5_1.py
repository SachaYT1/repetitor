f = open('24_1975.txt').read()
while 'PP' in f:
    f = f.replace('PP', 'P P')
c = f.split()
ans = 0
for string in c:
    ans = max(ans, len(string))
print(ans)