f = open('24_4627.txt').read()

f = f.replace('NPO', '*').replace('PNO', '*')
f = f.replace('P', " ").replace('N', " ").replace('O', ' ')

m = 0
s = f.split()
for string in s:
    m = max(m, len(string))
print(m)