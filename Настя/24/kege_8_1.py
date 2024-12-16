f = open('24_4602.txt').read()

f = f.replace('O', 'A').replace('C', 'B').replace('D', 'B')
f = f.replace('BA', '*').replace('B', ' ').replace('A', ' ')

m = 0
s = f.split()
for string in s:
    m = max(m, len(string))
print(m)