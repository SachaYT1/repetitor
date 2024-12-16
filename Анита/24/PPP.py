s = 'PPPPPPP'

s = s.replace('PPP', 'PP PP')
print(s)
c = s.split()
m = 0
for i in c:
    m = max(len(c), m)
print(m)


