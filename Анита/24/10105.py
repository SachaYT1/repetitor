f = open('24_10105.txt').readline()
s = f.split('T')
m = 0
count = 0
c = 100
for i in range(len(s)):
    if count == 101:
        m = max(m, c)
        c += len(s[i]) - len(s[i - 101])
        m = max(m, c)
    else:
        c += len(s[i])
        count += 1
print(m)
