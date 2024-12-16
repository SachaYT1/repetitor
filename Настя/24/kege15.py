f = open('24_4113.txt').read()

# while 'BB' in f:
f = f.replace('BB', '*').replace('*B', '*')
# while 'DD' in f:
f = f.replace('DD', '*').replace('*D', '*')

f = f.replace('A', ' ').replace('B', ' ').replace('D', ' ')
s = f.split()
c_max = 0
for i in s:
    c_max = max(c_max, len(i))
print(c_max)