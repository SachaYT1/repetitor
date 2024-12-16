f = open('24_2427.txt').read()
c = 1
c_max = 1
ans = f[0]
maxAns = ''

for i in range(1, len(f)):
    if f[i] < f[i - 1]:
        c += 1
        ans += f[i]
        if c > c_max:
            c_max = c
            maxAns = ans
    else:
        c = 1
        ans = f[i]
print(c_max)
print(maxAns)