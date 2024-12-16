ans = 0
for n in range(4, 10000):
    s = '1' + n * '8'
    while ('18' in s) or ('388' in s) or ('888' in s):
        s = s.replace('18', '1')
        s = s.replace('388', '83')
        s = s.replace('888', '3')

    if s.count('3') == 7:
        ans += n

print(ans)