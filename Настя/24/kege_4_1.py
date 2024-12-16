f = open('24_1428.txt').read()
a = f.replace('XY', ' ').replace('XZ', ' ')
c = a.split()
ans = 0
for string in c:
    ans = max(ans, len(string))
print(ans + 2)