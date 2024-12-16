f = open('24_9791.txt').readline()
c = m = 0
for i in range(len(f)):
    if f[i] in '123456789ABCDEF':
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
