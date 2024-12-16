from itertools import product

a = product('АКЛМНЯ', repeat=5)

sasha = '12345'
print(sasha[:2])
num = 1
ans = []
for i in a:
    s = ''.join(i)
    if s[:2] == 'МН':
        ans.append(num)
    num += 1

print(ans[-1] - ans[0] - 1)

