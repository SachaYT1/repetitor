f = open('24_4.txt').readline()

c1 = 0
c1_max = 0
for i in range(0, len(f) - 1, 2):
    if (f[i] + f[i + 1]) == 'SS' or (f[i] + f[i + 1]) == 'UU':
        c1 += 1
        c1_max = max(c1, c1_max)
    else:
        c1 = 0

c2 = 0
c2_max = 0
for i in range(1, len(f) - 1, 2):
    if (f[i] + f[i + 1]) == 'SS' or (f[i] + f[i + 1]) == 'UU':
        c2 += 1
        c2_max = max(c2, c2_max)
    else:
        c2 = 0

print(f'{c1_max} {c2_max}')
print(max(c1_max, c2_max))