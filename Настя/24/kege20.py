f = open('24_13715.txt').read()

l = 0
m = k = 0
for r in range(1,len(f)):
    if f[r - 1] + f[r] == 'AB':
        k += 1
    while k > 50:
        if f[l] + f[l + 1] == 'AB':
            k -= 1
        l += 1
    if k == 50:
        m = max(m, r - l + 1)
print(m)