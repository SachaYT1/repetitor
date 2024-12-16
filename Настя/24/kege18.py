f = open('24_2251.txt').read()

f = f.replace('D', ' ')
c = f.split()

ans = 0
for i in range(2, len(c)):
    len_posled = len(c[i - 2]) + len(c[i - 1]) + len(c[i]) + 2
    ans = max(ans, len_posled)
print(ans)
