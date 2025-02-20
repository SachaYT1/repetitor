f = open('4.txt').read()

l = 0
r = 0
count_a = 0
count_o = 0
ans = 0
len_posled = 0
while (r < len(f)):
    if f[r] == 'A':
        count_a += 1
    if f[r] == 'O':
        count_o += 1
    r += 1
    while (count_a > 100 or count_o > 100):
        if f[l] == 'O':
            count_o -= 1
        if f[l] == 'A':
            count_a -= 1
        l += 1
    ans = max(r - l, ans)
print(ans)