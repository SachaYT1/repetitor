f = open('24_4643.txt').read()

f = f.replace('B', 'A').replace('2', '1')
f = f.replace('11A', '*').replace('1', ' ').replace('A',' ')

s = f.split()
ans = 0
for string in s:
    ans = max(ans, len(string))
print(ans)