f = open('24_10105.txt').read()

l = m = k = 0
for r in range(len(f)):
    if f[r] == 'T':
        k += 1
    while k > 100:
        if f[l] == 'T':
            k -= 1
        l += 1
    if k == 100:
        m = max(m, r - l + 1)

print(m)