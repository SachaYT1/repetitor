f = open('24_8654.txt').readline()
m = prev = 0
for i in range(len(f) - 4):
    m = max(m, i - prev + 1)
    if f[i + 1] + f[i + 4] == 'BD':
        m = max(m, i + 3 - prev + 1)
        prev = i + 1
print(m)
