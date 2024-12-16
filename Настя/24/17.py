f = open('24_4546.txt').read()

f = f.replace('AAA', '*').replace('ABA', '*').replace('ACA', '*')
f = f.replace('CAC', '*').replace('CBC', '*').replace('CCC', '*')
f = f.replace('A', ' ').replace('B', ' ').replace('C', ' ')
c = f.split()
ans = 0
for string in c:
    ans = max(ans, len(string))
print(ans)