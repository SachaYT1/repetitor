s = 'PPPPPPP'
c = m = 2
for i in range(len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] != 'PPP':
        c += 1
        m = max(m, c)
    else:
        c = 2
print(m)