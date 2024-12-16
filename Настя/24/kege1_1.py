f = open('24_2420 (1).txt').read()
a = f.replace('C', ' ').replace('D', ' ')
c = a.split()
ans = 0
for string in c:
    ans = max(ans, len(string))
print(ans)